# By Quin Goins
# Begun December 12 2022
# Redistributeable under MIT license
"""This module was created with the intent to automate and script large portions of the General Chemistry I equations 
and Constants that were taughtt in Professor Benjamin Hession's class in the fall of 2022 at the University of Alabama in Huntsville.
Additional functions have been created for other various purposes."""
# The following functions pertain to temperatures in celsius and kelvin
def f2c(farenheit):
    """Takes a temperature in degrees farenheit as an argument and returns a temperature in degrees celsius."""
    farenheit = float(farenheit)
    celsius = (5/9)*(farenheit-32)
    return(celsius)
def c2f(celsius):
    """Takes a temperature in degrees celsius as an argument and returns a temperature in degrees farenheit."""
    celsius = float(celsius)
    farenheit = (celsius*9/5)+32
    return(farenheit)
def k2c(kelvin):
    """Takes a temperature in degrees kelvin as an argument and returns a temperature in degrees celsius."""
    kelvin = float(kelvin)
    celsius = kelvin - 273.15
    return(celsius)
def c2k(celsius):
    """Takes a temperature in degrees celsius as an argument and returns a temperature in degrees kelvin."""
    celsius = float(celsius)
    kelvin = celsius + 273.15
    return(celsius)
def csvSplit(line):
    line = line.strip() # removes excess whitespace
    lineList = line.split(',') # seperates the values in the lines delimited by commas into a list
    return(lineList)
def elementInfo(z):
    z=int(z)
    if z < 1 or z > 120: # not a valid atomic number
        return(-1) # error
    file = open('PubChemElements_all.csv','r',encoding='utf-8')
    headerRead = False # Bool for seperating header labels
    for line in file: # Executes once for each line in the file
        if headerRead: # executes if the header has already been stored
            if int(csvSplit(line)[0])==z: # executes if the atomic number of the entry is identical to that specified at function call
                data = csvSplit(line)
                break
        else: # executes if the header has not been read
            headerList = csvSplit(line)
            headerRead = True
    info = dict() # create empty dictionary to hold 
    for i in range(0,len(data)):
        print(i)
        info.update((headerList[i],data[i]))
    print(info)
    return(data)
elementInfo(6)