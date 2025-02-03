from pymarc import *

def main():
    while True:

        option = validate()

        if (option == 2):
            """This is the *correct* option"""

            print("good shit.")
            break  

        else:

            print("you missed that one, try another!")
            continue


def validate():
    """Takes an input and ensures its a positive integer. Returns said integer."""

    while True:
        value = input("Enter a positive integer : ")

        try:
            value = int(value)

        except:
            print("THAT WASN'T A POSITIVE INTEGER.")
            continue

        if(value <= 0):
            print("NUMBER IS ZERO OR NEGATIVE.")
            continue
        
        else:
            print("FUCK YEAH")
            return value
        
main()

