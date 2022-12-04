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
def newElement(z): # improved version of elementInfo using the csv module and dictReader
    """Takes the atomic number of an atom as input and returns data about it in a dictionary."""
    import csv # needed to eeficiently parse the data file
    z = int(z) # enforces data type
    if z < 1 or z > 118: # checks for validity of atomic number
        print(f'"{z}" is not a valid atomic number. Please check your code.')
        return(-1) # ends and signifies an error
    with open('PubChemElements_all.csv','r',encoding='utf-8') as dataFile: # automatically manages opening, closing, and accessing file
        csv_reader = csv.DictReader(dataFile) # reads each line of the csv file as a dictionary keyed to the header
        for line in csv_reader: # repeats for each line in the file after the first one
            if int(line['AtomicNumber']) == z: # checks if the current line is the target element
                return(line) # returns a dictionary of data about the element
print(newElement(117))