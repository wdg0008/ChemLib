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
def tempConverter(given,givenUnit='c',findUnit='k'):
    """tempConverter converts the numerical value of its first argument with asssociated units from the second argument
    into a corresponding output depending upon the desired unit of measurement specified in the third argument.
    By default, it will assume conversion from degrees celsius to kelvin.
    ARGUMENTS:
        given - a float reperesenting the numerical value of the given temperature
        givenUnit - a one-letter string reperesenting units of either celsius, farenheit, or kelvin for the data to convert
            (defaults to celsius)
        findUnit - a one-letter string reperesenting units of either celsius, farenheit, or kelvin for the desired output
            (defaults to kelvin)"""
    if given != float(given): # ensures the given data is a mathematically intelligible number
        print('Please input a valid float to be converted.')
        return('ERROR')
    else:
        given = float(given) # enforces float data type on input to prevent typeErrors later if it is an integer
    givenUnit = str(givenUnit).lower()
    findUnit = str(findUnit).lower()
    valid = ('c','f','k')
    if len(givenUnit) != 1 or len(findUnit) != 1 or givenUnit not in valid or findUnit not in valid: # checks for bad units
        print(f'Please use only one of the following as inputs: {valid}')
        return('ERROR')
    elif givenUnit == findUnit: # there is no conversion of units, so just returns original input
        return(given)
    match givenUnit: # checks the given units
        case 'c': # input is in degrees celsius
            match findUnit: # finds unit to convert to
                case 'f': # convert celsius to farenheit
                    return(c2f(given))
                case 'k': # convert celsius to kelvin
                    return(c2k(given))
        case 'f': # input is in degrees farenheit
            match findUnit: # finds unit to convert to
                case 'c': # convert farenheit to celsius
                    return(f2c(given))
                case 'k': # convert farenheit to kelvin
                    celsius = f2c(given)
                    return(c2k(celsius))
        case 'k': # input is in degrees kelvin
            match findUnit: # finds unit to convert to
                case 'c': # convert kelvin to celsius
                    return(k2c(given))
                case 'f': # convert kelvin to farenheit
                    celsius = k2c(given)
                    return(c2f(celsius))

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

# the following functions have to do with dictionaries
def dict_printer(dictin): # a cool function to print dictionaries without weird misalignment
    """dict_printer takes the values of each pair in a dictionary and prints them out on new lines with resizing justification.
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
        zeroCount = maxLength - len(newstring)+1 # calculates the number of spaces to be added for alignment, less one for the later space
        print(' '*zeroCount + f'{newstring}:'+ ' ' +f'{dictin[item]}') # prints the dict pair all nice and pretty-like and in line with all others

def dictFill(list):
    """dictFill returns a dictionary with the input list as keys and user-specified inputs as their values.
    Press enter once you have typed in the appropriate value to save it and begin typing the next one.
    ARGUMENTS:
        list - a list of strings or numbers to use as the keys of a dictionary
    RETURNS:
        dictionary - contains keys from the list and values input by the user
    OUTPUTS:
        instructions on what to do and the key that the data will currently be entered to"""
    dictionary = dict()
    maxLength = int() # initializes length checker to align text
    for item in list:
        if len(item) > maxLength:
            maxLength = len(item)
    print('Please enter the data values corresponding to each item below.')
    for item in list:
        spaceCount = maxLength - len(item)+1 # calculates the number of spaces to be added for alignment, less one for the later space
        dictionary[item] = float(input(' '*spaceCount + f'{item}: '))
    return(dictionary)

# The following lines of code pertain to the ideal gas law and asume usage of units specified in the constant function
def constant(name): # function that return the value of different constants for later equations
    """constant(name) will return eihter the planck constant, ideal gas constant, speed of light, or an error.
    ARGUMENTS:
        name - a one-letter string of either 'r', 'h', or 'c'
    OUTPUTS:
        Help messages corresponding to different forms of invalid input
    RETURNS:
        A float reperesenting one of the following:
        1. The ideal gas constant in (L*atm)/(mol*K)
        2. The planck constant in (J*s)
        3. The speed of light in (m/s)"""
    constants = ('r','h','c')
    if str(name) != name:
        print('Please only input a string.')
        return(-1)
    else:
        name = str(name) # forces string type
        if name not in constants: # input invalid
            print(f'Only the following are valid arguments: {constants}')
            return(-1)
        else: # the input is valid
            match constants.index(name): # finds index of argument in tuple of valid inputs
                case 0: # ideal gas law constant
                    return(0.0821) # liters times atmospheres per mol times kelvin
                case 1: # planck constant
                    return(6.626*10**(-34)) # joule seconds
                case 2: # speed of light
                    return(3*10**8) # meters per second

# these functions solve for a certain value of an ideal gas given all others
def solvePressure(gas): # takes dictionary with values for gas as input
    """solvePressure - solves for the pressure of an ideal gas given its other properties.
    ARGUMENTS:
        gas - a dictionary containing data about the gas with the following structure:
            gas = {
                'temperature':float,
                'volume':float,
                'amount':float
                }
    RETURNS:
        gas - same dictionary, but now with new/corrected pressure data
    OUTPUTS:
        NONE
    DEPENDENCIES:
        chem.constant"""
    # uncomment the following line if issues with dependencies
    # from chem import constant
    if dict(gas) != gas:
        print('This method may only be called on a dictionary object.')
        return(-1)
    gas['pressure'] = gas['amount']*constant('r')*gas['temperature']/gas['volume']
    return(gas)
def solveVolume(gas): # takes dictionary with values for gas as input
    """solveVolume - solves for the volume of an ideal gas given its other properties.
    ARGUMENTS:
        gas - a dictionary containing data about the gas with the following structure:
            gas = {
                'temperature':float,
                'pressure':float,
                'amount':float
                }
    RETURNS:
        gas - same dictionary, but now with new/corrected volume data
    OUTPUTS:
        NONE
    DEPENDENCIES:
        chem.constant"""
    # uncomment the following line if issues with dependencies
    # from chem import constant
    if dict(gas) != gas:
        print('This method may only be called on a dictionary object.')
        return(-1)
    gas['volume'] = gas['amount']*gas['temperature']*constant('r')/gas['pressure']
    return(gas)
def solveAmount(gas): # takes dictionary with values for gas as input
    """solveAmount - solves for the amount of an ideal gas given its other properties.
    ARGUMENTS:
        gas - a dictionary containing data about the gas with the following structure:
            gas = {
                'temperature':float,
                'volume':float,
                'pressure':float
                }
    RETURNS:
        gas - same dictionary, but now with new/corrected amount data
    OUTPUTS:
        NONE
    DEPENDENCIES:
        chem.constant"""
    # uncomment the following line if issues with dependencies
    # from chem import constant
    if dict(gas) != gas:
        print('This method may only be called on a dictionary object.')
        return(-1)
    gas['amount'] = (gas['pressure']*gas['volume'])/(constant('r')*gas['temperature'])
    return(gas)
def solveTemperature(gas): # takes dictionary with values for gas as input
    """solvePressure - solves for the temperature of an ideal gas given its other properties.
    ARGUMENTS:
        gas - a dictionary containing data about the gas with the following structure:
            gas = {
                'pressure':float,
                'volume':float,
                'amount':float
                }
    RETURNS:
        gas - same dictionary, but now with new/corrected temperature data
    OUTPUTS:
        NONE
    DEPENDENCIES:
        chem.constant"""
    # uncomment the following line if issues with dependencies
    # from chem import constant
    if dict(gas) != gas:
        print('This method may only be called on a dictionary object.')
        return(-1)
    gas['temperature'] = (gas['pressure']*gas['volume'])/(constant('r')*gas['amount'])
    return(gas)
dict_printer(solveTemperature(dictFill(['pressure','volume','amount'])))