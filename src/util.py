import os
"""
This class contains functions used in the other classes.
"""

"""
Clears the screen after asking the user to press enter.
"""
def clear():
    input("Press enter to continue.")
    os.system('cls' if os.name == 'nt' else 'clear')
    #thanks, https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    pass

def validate():
    """Requests an input and ensures it's a positive integer. Returns said integer."""

    try:
        value = int(input("GIMME NUMBER: "))

    except:
        print("THAT WASN'T A POSITIVE INTEGER.")
        return

    if(value <= 0):
        print("NUMBER IS ZERO OR NEGATIVE.")
        return

    else:
        return value
    

"""Takes a value and checks if its within the range of values. Used in menus. Inclusive.

Args:
floor -- The lower value not to be below.
ceil -- The higher value not to be exceeded.
val -- The number being tested.

Returns:
True -- If the value doesn't break the range.
False -- If the value does break the range.
"""
def within(floor, ceil, val):

    try:
        test = int(val)
    except:
        print("Oops, that probably wasn't a numnber.")
        return False
    if test < floor:
        print("Oops, the number was less than "+str(floor)+".")
        return False
    elif test > ceil:
        print("Oops, the number was higher than "+str(ceil)+".")
        return False
    else:
        return True

    
