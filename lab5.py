###############################################
# APS106  2022 - Lab 5 - Measurement Parser   #
###############################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """

    first = ''
    last = ''
    flag = True
    for i in email:
        if flag:
            if i != '.':
                first += i
            else:
                flag = False
        else:
            if i != '@':
                last += i
            else:
                break
    last = last.upper()
    first = first.upper()
    return last+','+first
    



###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
    """
    (str) -> int
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements
 
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    
    >>> count_measurements("Control, 7.5")
    1
    """
    counter = 0
    for i in s:
        if i == ',':
            counter += 1
    counter += 1
    return counter // 2



######################################
# Part 3 - Calculate Site Average    #
######################################

def calc_site_average(measurements, site):
    """
    (str, str) -> float
 
    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site, 
    return the average of the site measurements to one decimal place
    
    
    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    """
    count = count_measurements(measurements)
    m = measurements.split(',', count*2)
    for i in range(len(m)):
        if m[i][0] == ' ':
            m[i] = m[i][1:]
    ans = 0
    counter = 0
    for i in range(count):
        if m[i*2] == site:
            ans += float(m[i*2+1])
            counter += 1
    if counter == 0:
        return 0
    else:
        return round(ans / counter, 1)
    
    


###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as
    
        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...
    
    returns a string with the extracted information formatted as
    
        LASTNAME,FIRSTNAME,number of measurements,average pH of specified site
 
    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    'DOMINGUEZ,DINA,7,7.2'
    """
    count = count_measurements(measurement_info)
    m = measurement_info.split(',', count*2)
    for i in range(len(m)):
        if m[i][0] == ' ':
            m[i] = m[i][1:]
    count -= 1
    email = m[0]
    m = m[2:]
    name = email_to_name(email)
    ans = 0
    counter = 0
    for i in range(count):
        if m[i*2] == site:
            ans += float(m[i*2+1])
            counter += 1
    if counter == 0:
        return name + "," + str(count) + ',' + str(0)
    else:
        return name + "," + str(count) + ',' + str(round(ans / counter, 1))



## TODO: YOUR TEST CODE HERE - REMEMBER TO DELETE THESE LINES BEFORE SUBMITTING
