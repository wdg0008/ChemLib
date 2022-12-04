# By Quin Goins
# Begun December 12 2022
# Redistributeable under MIT license
"""This module was created with the intent to automate and script large portions of the General Chemistry I equations 
and Constants that were taught in Professor Benjamin Hession's class in the fall of 2022 at the University of Alabama in Huntsville.
Additional functions have been created for other various purposes."""
# The following functions pertain to temperatures in celsius and kelvin
def f2c(farenheit): # farenheit to celsius converter
    """Takes a temperature in degrees farenheit as an argument and returns a temperature in degrees celsius.
    ARGUMENTS:
        farenheit - temperature in degrees Farenheit
    OUTPUTS:
        NONE
    RETURNS:
        celsius - temperature in degrees celsius equivalent to input"""
    farenheit = float(farenheit)
    celsius = (5/9)*(farenheit-32)
    return(celsius)
def c2f(celsius): # celsius to farenheit converter
    """Takes a temperature in degrees celsius as an argument and returns a temperature in degrees farenheit.
    ARGUMENTS:
        celsius - temperature in degrees Celsius
    OUTPUTS:
        NONE
    RETURNS:
        farenheit - temperature in degrees Farenheit equivalent to input"""
    celsius = float(celsius)
    farenheit = (celsius*9/5)+32
    return(farenheit)
def k2c(kelvin): # kelvin to celsius converter
    """Takes a temperature in degrees kelvin as an argument and returns a temperature in degrees celsius.
    ARGUMENTS:
        kelvin - temperature in degrees Kelvin
    OUTPUTS:
        NONE
    RETURNS:
        celsius - temperature in degrees Celsius equivalent to input"""
    kelvin = float(kelvin)
    celsius = kelvin - 273.15
    return(celsius)
def c2k(celsius): # celsius to kelvin converter
    """Takes a temperature in degrees celsius as an argument and returns a temperature in degrees kelvin.
    ARGUMENTS:
        celsius - temperature in degrees celsius
    OUTPUTS:
        NONE
    RETURNS:
        kelvin - temperature in degrees Kelvin equivalent to input"""
    celsius = float(celsius)
    kelvin = celsius + 273.15
    return(kelvin)

# The following lines of code focus on data for each element of the periodic table
def newElement(z): # improved version of elementInfo using the csv module and dictReader
    """Takes the atomic number of an atom as input and returns data about it in a dictionary.
    ARGUMENTS:
        z - any integer between 1 and 118, inclusive
    RETURNS:
        line - a dictionary containing the first line of the csv values as keys and the data
        for element with atomic number z as values
    OUTPUTS:
        NONE"""
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
def dict_printer(dictin):
    """dict_printer takes the values of each pair in a dictionary and prints them out on new lines.
    ARGUMENTS:
        dictin: any dictionary
    RETURNS:
        NONE
    OUTPUT:
        Multiple lines of text reading `{key}: {value}` for each pair in dictin
        If dictin is not a dictionary, a message reminding the user to input the correct data type.
        Automatically justifies text of values to be in line with a few spaces after the longest key."""
    from string import ascii_lowercase, ascii_uppercase
    if dict(dictin) != dictin:
        print('Please check your code and make sure you are calling dictionary_printer on a dictionary and not some other data structure.')
    dictin = dict(dictin) # enforces data type of dictionary to allow respective methods to be called
    maxLength = int() # sets default length to fill at zero
    for item in dictin:
        if len(item) > maxLength:
            maxLength = len(item)
    for item in dictin: # each iteration will print a single key and its associated value
        newstring = str() # initializes an empty string to fill with correctly spaced words
        for letter in item: # iterates through each letter to add spaces between 
            if len(newstring) != 0: # executes if the first line has already been read
                if letter in ascii_uppercase and newstring[-1] in ascii_lowercase: # checks if the next letter is uppercase and the last letter was lowercase
                    newstring = newstring + " "+ letter # adds a space in between words
                else: # executes only for the first line (there is no last letter, so this was split to avoid index errors)
                    newstring = newstring + letter
            else:
                newstring = str(letter)
        zeroCount = maxLength - len(newstring)+1 # calculates the nu,ber of spaces to be added for alignment, less one for the later space
        print(' '*zeroCount + f'{newstring}:'+ ' ' +f'{dictin[item]}') # prints the dict pair all nice and pretty-like and in line with all others
dict_printer(newElement(117))