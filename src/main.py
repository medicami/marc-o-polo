import os
import csv
import tkinter as tk
from tkinter.filedialog import *
from compare import *
from convert import *
from util import *

def main():
    window = tk.Tk()
    window.attributes('-topmost', 1)
    window.withdraw()
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
                clear(False)
                target = coolerGetCSV()
                if target != None:
                    readCSV(target)

                pass
            case 2:
                print("This is the comparison option.")
                clear(False)
                '''
                message = "target marc file (to be compared to master)."
                targetMarc = getMarc(message)
                message = "master marc file (to compare against)."
                targetMaster = getMarc(message)
                '''
                print("Please choose the MARC file you want to compare using (your master file)")
                targetMaster = askopenfilename(title="Please choose the MARC file you want to compare using (master file).",filetypes=[("MARC files", "*.mrc")])
                print("Please choose the MARC file you want to compare using (your master file)")
                targetMarc = askopenfilename(title="Please choose the MARC file you want to compare against (testing file).",filetypes=[("MARC files", "*.mrc")])


                compare(targetMarc, targetMaster)

                pass
            case 3:
                peck()
                break
            case 84:
                joke()
            case _:
                pass
                
                
                

        clear()
        continue


"""*** Note, the functions from here are just test functions for practice. ***"""

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
    with open(abspath, newline='', errors='ignore') as csvfile:
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

main()
#LET'S REV UP THOSE FRYERS!