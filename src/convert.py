import pymarc
import os
import csv
from util import *

"""
This class is dedicated to converting the information within a csv file into a marc file.
Only some of the information from each row will be needed.
First step is to get the names of the files from the csv folder and show them to the user.


"""
def convert():
    


    
    pass

"""
User should be able to pick which of the files they want.
Remember that lists are zero inclusive, so everything is offset by -1 (0,1,2,etc.).
Input can be exactly as typed, but if wishing to use zero exclusive, offset by +1.


Return:
target -- the string which identifies the .csv file
"""
def getCSV():
    relpath = "../../data/csv"
    abspath = os.path.join(__file__,relpath)
    dir = os.listdir(abspath)
    dir.sort()
    target = ""

    match(len(dir)):
        case 0: #there is nothing in the directory
            print("Unfortunately there's nothing in the data/csv folder.")
            clear()
            pass
        case 1: #there is only one file in the directory
            while True:
                print("There's exactly one file available, "+dir[0]+", do you want to convert this?")
                print("""
                    [0] DO IT
                    [1] NOPE""")
                
                try:
                    choice = int(input("Enter a number: "))
                except:
                    print("Oh, maybe you didn't type a number?")
                    clear()
                    continue
                if choice == 0:
                    target = abspath+"/"+dir[0]
                    print("Target file set: "+target)
                    clear()
                    return target
                elif choice == 1:
                    print("Let's skedaddle!")
                    clear()
                    break
                else:
                    print("Oh, that number wasn't an option.")
                    clear()
                
        case _: #there are many files in the directory
            while True:
                dirSize = range(len(dir))
                print("""
                    Here are the files in data/csv, which one do you want to convert?
                    """)
                for i in dirSize:
                    print("["+str(i)+"]"+" "+dir[i])

                
                choice = input("Enter a number corresponding to the thing you want (0 to "+str(len(dir)-1)+"): ")
                if within(0,len(dir)-1,choice)==False:
                    clear()
                    continue
                else:
                    target = abspath+"/"+dir[int(choice)]
                    print("Target file set: "+target)
                    clear()
                    return target

"""
Using a string to identify the target file, read the .csv file and strip the important information out.
Put the information into a .marc file. Each row corresponding to a new record in the file."""
def readCSV(target):
    with open(target, newline='') as csvfile:
        
        pass
    pass
            


"""
We can read from a list of files in a directory. If the user specifies a string for a filename, this can check to see if that file
exists in a given directory, and can potentially ask them if they want to reconsider their choice. In this program, I don't think
this will be used anywhere except for making .marc files, but might as well have the option to allow different dirnames.

Args:
filename -- the name of the file being created by the user.
dirname -- the directory the file is going to.

Return:
True -- if the user wants to write to the thing or no existing file is found.
False -- if an existing file is found and the user does not want to overwrite.
"""
def rusure(filename, dirname):
    pass