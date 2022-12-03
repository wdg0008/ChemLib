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
file = open('scratch.txt','w')
for i in range(1,121):
    file.write(str(i)+'\n')
file.close()
# https://inventwithpython.com/bigbookpython/project53.html