# Unit Converter
system = input('What system of units are you using? Tpye SI for metric or US for customary.').lower()
usBase = { # defines the base units for the customary system for this program
'weight':'pounds',
'mass':'slugs',
'time':'seconds',
'distance':'feet',
'temperature':'farenheit',
'work':'foot-pounds',
'angle':'degrees'
}
siBase = {
'time':'second',
'distance':'meter',
'mass':'kilogram',
'current':'ampere',
'temperature':'kelvin',
'amount':'mol',
'intensity':'candela',
'angle':'radians'
}
siPrefixes = {
    'yotta':24,
    'zetta':21,
    'exa':18,
    'peta':15,
    'tera':12,
    'giga':9,
    'mega':6,
    'kilo':3,
    'hecto':2,
    'deca':1,
    'deci':-1,
    'centi':-2,
    'milli':-3,
    'micro':-6,
    'nano':-9,
    'pico':-12,
    'femto':-15,
    'atto':-18,
    'zepto':-21,
    'yocto':-24
}
print(f'The following are acceptable dimensions of measurement: ')
match system: # checks what unit system is in use
    case 'si':
        for item in siBase:
            print(item+', ')
        dimension = input('What are you measuring?').lower()
        unit = siBase[dimension]
    case 'us':
        for item in usBase:
            print(item+', ')
        dimension = input('What are you measuring?').lower()
        unit = usBase[dimension]
value = float(input(f'How many {unit} do you have?'))
