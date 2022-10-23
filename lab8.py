###################################################
# APS106 - Winter 2022 - Lab 8 - Corner Detection #
###################################################

from lab8_image_utils import display_image, image_to_pixels
from operator import itemgetter


def OneD_to_TwoD(img, width, height):
    last = 0
    matrix = []
    for i in range(len(img)):
        if (i % height == 0 and i != 0):
            matrix.append(list(img[last:(i)]))
            last = i
    matrix.append(list(img[-1 * height:]))
    return matrix


def Kernel_Product(kernel, matrix):
    Dot_Sum = []
    for i in range(len(kernel)):
        for j in range(len(kernel[0])):
            Dot_Sum.append(kernel[i][j] * matrix[i][j])

    return (int(sum(Dot_Sum)))


def TwoD_to_OneD(matrix):
    Empty = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            Empty.append(matrix[i][j])

    return Empty


def Euclidean_distance(List_A, List_B):
    Sum = ((List_A[0] - List_B[0]) ** 2 + (List_A[1] - List_B[1]) ** 2) ** (1 / 2)
    return Sum


def Add_Zeros(List):
    zeros = []
    for i in range(len(List)):
        List[i].insert(0, 0)
        List[i].insert(len(List) + 2, 0)
    for n in range(len(List[0])):
        zeros.append(0)
    List.insert(0, zeros)
    List.insert(len(List) + 1, zeros)

    return (List)

################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################

def rgb_to_grayscale(rgb_img):
    """
    (tuple) -> tuple
    
    Function converts an image of RGB pixels to grayscale.
    Input tuple is a nested tuple of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation
    
        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B
    
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be *rounded* to the nearest
    integer.
    """
    
    ## TODO complete the function
    gray_image = []  

    for pixel in rgb_img:              
        R, G, B = pixel                
        gray_pixel = (0.3*R + 0.59*G + 0.11*B)
        gray_pixels = round(gray_pixel)
        gray_image.append(gray_pixels)

    gray_image = tuple(gray_image)
    return gray_image


############################
# Part 2b - Dot Product    #
############################

def dot(x,y):
    """
    (tuple, tuple) -> float
    
    Performs a 1-dimensional dot product operation on the input vectors x
    and y. 
    """
    
    ## TODO complete the function
    dotp = 0
    for i in range(len(x)):
        dotp += (x[i]*y[i])
    return float(dotp)

def get_coord_rgb(img, x, y, width, height):
    '''
    (list, int, int, int, int) -> int
    '''
    # Note: returns None if given coord is out of bounds.
    if (x < 0 or x >= width) or (y < 0 or y >= height):
        return

    return img[y * width + x]
    
    


######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (tuple, int, int, tuple, int) -> tuple
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a tuple of pixels from the
    image.
    
    img is a tuple of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element tuple defining a pixel coordinate
    N is the height and width of the segment to extract from the image
    
    """
    ## TODO complete the function
    start_row = centre_coordinate[1] - (N // 2)
    end_row = start_row + N
    start_col = centre_coordinate[0] - (N // 2)
    end_col = start_col + N
    new_img = []
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            new_img.append(get_coord_rgb(img, col, row, width, height))

    return tuple(new_img)
    

######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (tuple, int, int, tuple) -> tuple
    
    Apply the kernel filter defined within the two-dimensional tuple kernel to 
    image defined by the pixels in img and its width and height.
    
    img is a 1 dimensional tuple of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional tuple defining a NxN filter kernel, n must be an odd integer
    
    The function returns the tuple of pixels from the filtered image
    """

    ## TODO complete the function
    N = len(kernel)
    new_img = []
    for y in range(height):
        for x in range(width):
            segment = extract_image_segment(img, width, height, [x, y], N)
            total = 0
            if not (None in segment):
                # Go through the NxN kernel
                for row in range(N):
                    for col in range(N):
                        total += segment[row * N + col] * kernel[row][col]
            new_img.append(round(total))

    return tuple(new_img)


###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (tuple, tuple) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Ix and Iy are  lists each containing 9 integer elements each.

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (tuple, int, int, float) -> tuple
    
    Computes the corner strength of each pixel within an image
    and returns a tuple of potential corner locations. Each element in the
    returned tuple is a two-element tuple containing an x- and y-coordinate.
    The coordinates in the tuple are sorted from highest to lowest corner
    strength.
    """
    
    # perform vertical edge detection
    vertical_edge_kernel = ((-1, 0, 1),
                            (-2, 0, 2),
                            (-1, 0, 1))
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = ((-1,-2,-1),
                              ( 0, 0, 0),
                              ( 1, 2, 1))
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    border_sz = 1
    corners = []
    for i_y in range(border_sz, height-border_sz):
        for i_x in range(border_sz, width-border_sz):
            Ix_window = extract_image_segment(Ix, width, height, (i_x, i_y), 3)
            Iy_window = extract_image_segment(Iy, width, height, (i_x, i_y), 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                #print(corner_strength)
                corners.append([corner_strength,(i_x,i_y)])

    # sort
    corners.sort(key=itemgetter(0),reverse=True)
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return tuple(corner_locations)


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (tuple, float) -> tuple
    
    Filters any corners that are within a region with a stronger corner.
    Returns a tuple of corner coordinates that are at least min_distance away from
    any other stronger corner.
    
    corners is a tuple of two-element coordinate tuples representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    
    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    
    ## TODO complete the function
    F = []
    F.append(corners[0])
    print("F: ", F)
    print("length: ", len(F))

    for i in range(len(corners)):

        if (Euclidean_distance(F[i - 1], corners[i]) >= min_distance):
            F.append(corners[i])

    return tuple(F)
    
