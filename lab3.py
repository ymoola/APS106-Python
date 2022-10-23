##############################
# APS106 Winter 2022 - Lab 3 #
##############################
import math

def circle_overlap(circ1_centre_x, circ1_centre_y, circ1_radius,
                    circ2_centre_x, circ2_centre_y, circ2_radius):
    """
    (int, int, int, int, int, int) -> str

    Function determines whether two circles overlap. When circles
    overlap, the function checks for the following scenarios
        1. The two circles perfectly overlap
        2. The first circle is contained within the second
        3. The second circle is contained within the first
        4. The circle have overlapping area, but neither is completely
           contained within the other
    
    Function inputs represent x and y coordinates circle centres and their
    radii (see lab document)
           
    The function returns a string describing the overlap scenario
    
    >>> circle_overlap(0,1,3,6,4,1)
    'no overlap'
    
    >>> circle_overlap(0,1,3,0,1,3)
    'identical circles'
    
    >>> circle_overlap(1,1,10,6,7,1)
    'circle 2 is contained within circle 1'
    
    >>> circle_overlap(-1,-2,2,0,0,11)
    'circle 1 is contained within circle 2'
    
    >>> circle_overlap(1,-2,2,-4,0,5)
    'circles overlap'
    """

    
 
    
    # TODO your code here
    circum = math.sqrt((circ1_centre_x - circ2_centre_x)**2 + (circ1_centre_y - circ2_centre_y)**2)
    if circ1_centre_x == circ2_centre_x and circ1_centre_y == circ2_centre_y and circ1_radius == circ2_radius:
        return 'identical circles'
    elif circum <= circ1_radius-circ2_radius:
        return 'circle 2 is contained within circle 1'
    elif circum <= circ2_radius-circ1_radius:
        return 'circle 1 is contained within circle 2'
    elif circum < circ1_radius + circ2_radius:
        return 'circles overlap'
    else:
        return 'no overlap'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
