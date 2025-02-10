import pymarc
import os
import csv


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
String -- the string which identifies the .csv file
"""
def getCSV():
    relpath = "../../data/csv"
    abspath = os.path.join(__file__,relpath)

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