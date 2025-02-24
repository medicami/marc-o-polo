
import os
import csv
from util import *
from pymarc import Record, Field, Subfield, Indicators

"""
This class is dedicated to converting the information within a csv file into a marc file.
Only some of the information from each row will be needed.
First step is to get the names of the files from the csv folder and show them to the user.
"""


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
                    [1] DO IT
                    [2] NOPE""")
                
                try:
                    choice = int(input("Enter a number: "))
                except:
                    print("Oh, maybe you didn't type a number?")
                    clear()
                    continue
                if choice == 1:
                    target = abspath+"/"+dir[0]
                    print("Target file set: "+target)
                    clear()
                    return target
                elif choice == 2:
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
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #It turns out that working with a csv.reader object is like working with a cactus that's on fire in a cloud of sulfuric acid. So let's just make it a list.
        readme = list(reader)
        
        """We want to show the first row to the user and ask them if they want to use it. This isn't really necessary if we know exactly
        what our data is going to look like, but this would be something that would improve the usablility of the thing in a practical setting."""
        
        while True:
            print("This is the first row of the data file:\n"+str(readme[0])+"\nDo you want to use this for a record?")
            print("""
                [1] YES
                [2] NO""")
            choice = validate()
            match(choice):
                case 1:
                    #Nothing happens here because nothing needs to happen.
                    print("You will use the first row.")
                    pass
                case 2:
                    #Skip the first row
                    print("You will not use the first row.")
                    readme.pop(0)
                    
                    pass
                case _:
                    print("Uh, that wasn't one of the options.")
                    continue
            break
        clear()

        #Now we need to determine the pattern for what each column will be.
        fieldPat = []

        for i in readme[0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print("Please choose what this be in the MARC file: "+str(i)+".")
                print("""
                        [1] ISBN
                        [2] TITLE
                        [3] MAIN ENTRY
                        [4] DON'T USE""")
                choice = validate()
                if within(1,4,choice)==False:
                    print("Please try that again.")
                    clear()
                    continue
                else:
                    fieldPat.append(choice)
                    break


        #It's finally time to start using Pymarc. We have the rows and the patterns they will follow, so now we just have to make the records column by column.
        clear()
        name = input("Please give the new MARC file a name (no extension): ")
        relpath = "../../data/marc/"+str(name)+".mrc"
        #Note to self, I'm aware that certain characters are not allowed for file names, I don't know how this will handle it.
        abspath = os.path.join(__file__, relpath)
        with open(abspath, 'ab') as marc:
            for row in readme:

                record = Record()
                for i in range(0,len(fieldPat)-1):
                    match(fieldPat[i]):
                        case 1:
                            #ISBN
                            record.add_field(
                                Field(
                                    tag = '020',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=row[i])]
                                )
                            )
                            pass
                        case 2:
                            #TITLE
                            record.add_field(
                                Field(
                                    tag = '245',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=row[i])]
                                )
                            )
                            pass
                        case 3:
                            #MAIN ENT
                            record.add_field(
                                Field(
                                    tag = '100',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=row[i])]
                                )
                            )
                            pass
                        case 4:
                            #SKIP THIS
                            pass

                    marc.write(record.as_marc())
                    pass




        
        






"""
We can read from a list of files in a directory. If the user specifies a string for a filename, this can check to see if that file
exists in a given directory, and can potentially ask them if they want to reconsider their choice. In this program, I don't think
this will be used anywhere except for making .marc files, but might as well have the option to allow different dirnames.

Args:
filename -- the name of the file being created by the user.

Return:
True -- if the user wants to write to the thing or no existing file is found.
False -- if an existing file is found and the user does not want to overwrite.
"""
def rusure(filename):

    pass