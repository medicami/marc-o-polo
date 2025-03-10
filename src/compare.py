from pymarc import *
import os
import re
from util import *
#from convert import getCSV
from tkinter.filedialog import *

"""
This part of the program will read from two different marc records, one is a master file and one is a comparison file.
The comparison file contains brief records made from items being received by the company for processing.
The master file contains fuller records made by cataloguers that are meant to be reused.

By comparing unique aspects of each record (ISBN, most likely) we can determine which records already exist in the master file
that can be reused for these new items. These should be placed into a new file to represent the batch with master records.

Read from the test file and extract a record. Then parse through the master file and compare to each. When a match is found,
extract from the master and record to a new file. End parse. If nothing is found, end parse and add the test file record to
the new one.

Easy as pie, right?

Args:
first - the target file to compare against a master file.
second - the master file to compare to the target file.
"""
def compare(first, second):

    reader1 = MARCReader(open(first, 'rb'))
    reader2 = MARCReader(open(second, 'rb'))

    name = asksaveasfilename(title="Please choose where to save the new MARC file.", defaultextension=".mrc", filetypes={("MARC file", "*.mrc")})
    #relpath = "../../data/marc/"+str(name)+".mrc"
    #abspath = os.path.relpath(os.path.join(__file__, relpath))
    

    firstMatch = False

    for thing1 in reader1:
        for thing2 in reader2:

            if thing2.isbn == thing1.isbn and firstMatch == False:
                writeMe = open(name, 'wb')
                firstMatch = True

            if thing2.isbn == thing1.isbn:
                writeMe.write(thing2.as_marc())
                break
                
            pass
        pass
    
    reader1.close()
    reader2.close()
    if firstMatch == True:
        writeMe.close()
        print(f"If this printed, then all ended well.")
    else:
        print(f"If this printed, then no match was found between the two files, {os.path.relpath(first)} and {os.path.relpath(second)}.")
    pass

"""
Essentially a copy of getCSV from the convert file, but with the data/marc folder as the target. Additionally, this takes an argument
which should be a string to be printed on the screen to let the user know what thing they are picking.
"""
'''
def getMarc(message):
    relpath = "../../data/marc"
    abspath = os.path.join(__file__,relpath)
    dir = os.listdir(abspath)
    dir.sort()
    target = ""

    match(len(dir)):
        case 0:
            print("Unfortunately, there are no files in the data/marc folder.")
            return None
            
        case 1:
            print("Unfortunately, there's only one file in the data/marc folder.")
            return None
            
        case _:
            while True:
                dirSize = range(len(dir))
                print(f"Now selecting {message}.")
                print("""
                    Here are the files in data/marc, which one do you want to use?
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
            pass
    pass
'''
