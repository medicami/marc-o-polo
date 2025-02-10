import pymarc
import os
import csv
from compare import *

def main():
    
    while True:
        print(
            #it turns out when they said triple quotations were literal strings, they weren't kidding.
            """
            WILKOMMEN, COMPUTER WIZARD.
            
            CHOOSE YOUR DESTINY:
            [1] CONVERT CSV TO .MARC
            [2] COMPARE .MARC FILES
            [3] GET ME OUT OF HERE
            """
        )
        option = validate()

        match option:
            case 1:
                print("This is the conversion option.")
                
                pass
            case 2:
                print("This is the comparison option.")
                
                pass
            case 3:
                print("PECK")
                clear()
                break
            case _:
                pass
                
                
                

        clear()
        continue

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
        
def read_csv():
    """
    Receives a path to a .csv file and opens it, separating and storing its data.
    From what I know about the csv module, it is encouraged to use the newline='' parameter.

    Open the file as a csvfile, use a csv.reader to read, csv.writer to write.
    """
    print("########READCSV START")

    relpath = "../../data/csv/dummy"
    print(__file__)
    print(os.path.join(__file__, relpath))
    abspath = os.path.join(__file__, relpath)
    print(abspath)
    with open(abspath, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',', quotechar='*')
            for thing in read:
                print("!".join(thing))

            
    pass

def getFiles():
    """
    This is a testing function to see how we can grab the names of files from a directory.
    The purpose of this would be to allow a user to select from a list of files in the data directory,
    rather than be forced to write the absolute path to a file, which would be a PITA.

    Clearly, we can use os.listdir, to get a list of things (literally in a list object), then output this
    into some kind of menu that lets the user pick which one. Then we just have to concat the name of the file
    to a string that makes up the absolute path. Easy?
    """
    print("######## FUNC START")
    dir = os.path.join(__file__,"../../data/csv")
    print(dir)
    things = os.listdir(dir)
    for thing in things:
        print(thing)

    pass



