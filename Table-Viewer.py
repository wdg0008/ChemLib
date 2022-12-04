# Periodic Table Viewer
# Begun 12/04/2022
# imports chem.py and allows the user to tyoe in an atomic number to get information about the associated element.
from chem import dict_printer, newElement
while True:
    print('''\n                  Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    ask = input('Enter an atomic number or element name for info or tpye `q` to quit: ')
    if ask.lower() == 'q':
        break
    dict_printer(newElement(ask)) # grabs information about the element form the csv file and prints it
    