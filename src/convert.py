import re
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
    dir = os.listdir(os.path.relpath(abspath))
    dir.sort()
    target = ""

    match(len(dir)):
        case 0: #there is nothing in the directory
            print("""
                  Unfortunately there's nothing in the data/csv folder.
                  """)
            clear()
            return None
        case 1: #there is only one file in the directory
            while True:
                print("""
                      There's exactly one file available, "+dir[0]+", do you want to use this?
                      """)
                print("""
                    [1] DO IT
                    [2] NOPE
                      """)
                
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
                    Here are the files in data/csv, which one do you want to use?
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

    with open(target, 'r', newline='', errors='ignore') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #It turns out that working with a csv.reader object is like working with a cactus that's on fire in a cloud of sulfuric acid. So let's just make it a list.
        readme = list(reader)
        
        """We want to show the first row to the user and ask them if they want to use it. This isn't really necessary if we know exactly
        what our data is going to look like, but this would be something that would improve the usablility of the thing in a practical setting."""
        
        while True:
            print("\nThis is the first row of the data file:\n"+str(readme[0])+"\nDo you want to use this for a record?\n")
            print("""
                [1] YES
                [2] NO
                  """)
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
                    clear()
                    continue
            break
        clear()

        #Now we need to determine the pattern for what each column will be.
        usePat = [] #Store True or False if a column is going to be used or ignored, True if yes, False if no.
        fieldPat = [] #Store the string representing the field code for this column, e.g., 100, 245. 020
        subfieldPat = [] #Store the string representing the subfield for this column, e.g., a, b, d, p

        for i in readme[0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print(f"\nDo you want to include this in the MARC file: [ {str(i)} ] ?\n")
                print("""
                        [1] YES
                        [2] NO
                      """)
                choice = validate()
                if choice == False:
                    continue
                elif within(1,2,choice)==False:
                    print("Please try that again.")
                    clear()
                    continue
                elif choice==1:
                    usePat.append(True)
                    clear(True)

                    while True:
                        print(f"Please specify what FIELD CODE this [ {str(i)} ] will go into, e.g., 020, 100, 245, etc.")
                        
                        field = validate()
                        if field == False:
                            continue
                        elif within(1,999,field)==False:
                            print(f"Oops, your number ( {str(field)} ) is probably not a field code.")
                            clear()
                            continue
                        else:
                            fieldPat.append(field)
                            break
                    clear()

                    while True:
                        print("Field code: "+str(field))
                        print(f"Please specify what SUBFIELD this [ {str(i)} ] will go into, e.g., a, b, c, etc.")
                        
                        sub = validateSubField()
                        if sub == False:
                            clear()
                            continue
                        else:
                            subfieldPat.append(sub)
                            break
                    clear(True)
                    

                else:
                    usePat.append(False)
                    fieldPat.append(None)
                    subfieldPat.append(None)
                    pass
                
                #End of while
                break


        #It's finally time to start using Pymarc. We have the rows and the patterns they will follow, so now we just have to make the records column by column.
        
        
        name = input("Please give the new MARC file a name (no extension): ")
        relpath = "../../data/marc/"+str(name)+".mrc"
        #Note to self, I'm aware that certain characters are not allowed for file names, I don't know how this will handle it.
        abspath = os.path.join(__file__, relpath)
        with open(abspath, 'wb') as marc:

            for row in readme:
                #This iterates once for each row in the CSV
                record = Record()

                for i in range(0,len(usePat)):
                    #This iterates once for each column in the row (0 to the length of the pattern list minus 1)

                    v = re.sub("\(.*", "", str(row[i])).strip()
                    print(i)

                    #For some reason, this is an invalid escape sequence. But it still prints fine...
                    if usePat[i]==True:

                        match fieldPat[i]:
                            case '100':
                                #Main entry is title case
                                v = v.title()
                                pass
                            case '245':
                                #Titles are sentence case
                                v = v.capitalize()
                                pass
                            case _:
                                v = v.upper() #probably redundant but why not
                                pass

                        if record.get(str(fieldPat[i]))==None:
                            record.add_ordered_field(
                                Field(
                                        tag = str(fieldPat[i]),
                                        indicators = Indicators(' ',' '),
                                        subfields = [Subfield(code=str(subfieldPat[i]), value=v)]
                                    )
                            )
                        else:
                            """
                            I had intended to format subfields intended for prices to force 2 decimal places,
                            as it was when I catalogued at ULS, but evidently this is just way too specific.

                            if v.isdigit():
                            v = str(f'{float(v):.2f}')
                            pass
                            """

                            record.get(str(fieldPat[i])).add_subfield(
                                str(subfieldPat[i]), v
                            )
                        
                    else:
                        #do nothing
                        pass
                #For ends here

                marc.write(record.as_marc())
            #For ends here

    print(f"debug\n{usePat}\n{fieldPat}\n{subfieldPat}\n")
    print("If this prints, the file was successfully created at: "+str(os.path.relpath(abspath)))
    print("Note: this program will not do the following:\n\nRecognize proper nouns.\nAdd indicators.\nDo almost any error checking.\n\nPlease verify the output!\n")
    """ OLD SOLUTION
                    match(fieldPat[i]):
                        case 1:
                            #ISBN
                            record.add_ordered_field(
                                Field(
                                    tag = '020',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=v)]
                                )
                            )
                            pass
                        case 2:
                            #TITLE
                            record.add_ordered_field(
                                Field(
                                    tag = '245',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=v.capitalize())]
                                )
                            )
                            pass
                        case 3:
                            #MAIN ENT
                            record.add_ordered_field(
                                Field(
                                    tag = '100',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=v.title())]
                                    
                                )
                            )
                            pass
                        case 4:
                            #LOCAL FIELD
                            record.add_ordered_field(
                                Field(
                                    tag = '900',
                                    indicators = Indicators('/','/'),
                                    subfields = [Subfield(code='a', value=v.upper())]
                                    
                                )
                            )
                            pass
                        case 5:
                            pass
                        """
                    
#End of function




        
        






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