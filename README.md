# marc-o-polo
A small project to convert Linux datafiles containing bilbiographic data into MaRC files or other usable formats.

## The Problem
When books are received, information about them comes in a datafile on a Linux server. The file itself is essentially unusable for the cataloguers and other staff, who typically do their work on Windows machines. In order to convert this information into a usable formate for the other staff to use, information for individual books is printed out onto receipts and placed inside of the items for future processing.

## The Goal
To find a method of converting these datafiles into a usable format. The theoretical minimum would be to extract the information from the datafiles and export it to a Windows compatible format, such as an Excel spreadsheet, comma separated value .txt file, or whatever. In a perfect world, this information could be used to create template MaRC records, allowing for certain fields to be filled in automatically using information from the datafile.

## The Plan
The practicality of this project hinges on whether or not any common programming languages offer support for the original datafiles. Given that (as of February 2) I haven't heard any response from the client, I am going to proceed with the project in theoretical terms. With some cursory research, there is a Python module called Pymarc, which provides utilities for creating MaRC records using the Python language. If inputting information from the datafile is as easy as this, I am cautiously optimistic about the feasability of this project. If I were to start making the program, I would likely break it down into the following steps:

* Stage 0: Planning, outlining what inputs and outputs will be involved, what functionality to implement, pseudocode, etc.
* Stage 1: Can we read from the datafile at all.
* Stage 2: Try taking the input from the datafile and outputting it into another file format, such as .xlsx, .csv, .txt, etc.
* Stage 3: MaRC, creating a MaRC record using Pymarc based on information from variables in code.
* Stage 4: Taking the input from the datafile, assigning them to the variables, and seeing if it results in a working .marc file.
* Stage 5: Combining the previous steps into a single program that can take one input file and output one output file.
* Stage 6: Make the program more user friendly, ideally not requiring command line/terminal and usable as an executable.
* Stage 7: Make the program pretty with an actual GUI, probably definitely not feasible in the span of the class. This is natively available to code in Python with Tkinter, but looks (with all due respect) like a nightmare.

Any actual code is to be here: https://github.com/medicami/marc-o-polo

# "Literature" Review
Python is the language of choice for this project. The main reason being is that it's new and shiny and cool. On a more serious note, it is a relatively modern language with support for lots of additional functionality created by other people through modules. Python is more optimized than a language like Java, but a lot more intuitive and easy to learn compared to C++. It's also just different from what I learned with (Java), so this is a good learning opportunity.

If you have literally no experience with object oriented coding, I will attempt to explain plainly. We write code to give instructions to the computer. When you have some task you want to do many times, instead of rewriting that code every time you need it, we make a function with code in it, and then write the name of the function to "call" it. Calling the function essentially tells the computer to go over to that function and run the code inside of it. Other people have written code into functions and let other people use them, in Python these are called modules. The modules this project relies on most are the "csv" and "pymarc" modules.

CSV is a format that has been used for a very long time but has essentially no standardization, sometimes people don't even use commas to separate their values. Despite this, the csv module of Python allows a fair amount of customization to process different files, assuming we know ahead of time what the formatting will look like. Thankfully, this module is native to Python, so no additional installs are required for it. We're going to need to read from csv, but probably not write, so we'll mostly be relying on csv.reader objects to grab data from our files.

Pymarc is a module created by many people and can be found here https://gitlab.com/pymarc/pymarc. Pymarc will (hopefully) allow us to read from marc files and write to them. The main uses of this will be: writing to a marc file using data extracted from a csv, reading from a marc file and placing its information into a list, comparing the data from the csv marc to another marc file and identifying which ones exist in both (likely using ISBN). While it would be easier to just predict what fields/subfields each piece of the csv file should go into, it would be nice to allow the user to specify where each thing should go. Tags, field codes, and indicators are all strings, so substituting these with variables should be easy, it will just be annoying to apply verification to them to prevent issues.

# Converting from CSV to MARC
The program is currently in a state where it is able to convert CSV files to MARC. It is undoubtedly very primitive in how it does this, basically reading the rows from the CSV and turning it into text to throw into the MARC file: it does not do much validation on the finished output to determine if there are mistakes or anything like that.

CSV files are to be put into the data/csv folder. Output files will be placed in the data/marc folder. There is currently some limitations on where you can specify each field will go; the program will, in fact, ask you where each field in the row should go in the MARC file (it only asks for the first row) and then applies this to the entire file. I'm impressed at how fast it can go considering the test file is over four thousand rows long, but I guess computers are just magical like that.

Current foreseeable improvements: there is no validation for the name you put in for the name of the MARC file, which means that it will indescriminately overwrite things and will probably explode if you attempt to use illegal characters for filenames. ~~It would also be nice for the user to be able to specify what the indicators and sub-fields could be, the question is mostly where would this be stored.~~

After some additional effort, the program now asks the user for each field they want to use the code and subfield code. It would totally be possible to allow the user to specify indicators, except indicators vary for each field which would be incompatible for this tool meant to process an extremely large number of records quickly. You'd have to specify the indicators for every title and such, which wouldn't be fast at all. Additionally, I would have liked to format price numbers to two decimal places, but this would require asking the user every time a field is entered what kind of formatting they want or assuming a certain field/subfield combination is a price. I think the most practical way you would implement this is to ask the user in a different part of the program to set a specific field/subfield combo to be prices, then apply this when this combination occurs in the record. It's certainly feasible to have global settings like that, but I have other priorities right now.

# Comparing .mrc Files
One feature of the program that is tentatively being developed is the ability to compare two different .mrc files. The most instinctive idea would be to compare just the ISBNs, which is pretty simple since they're unique by design.

There is a utility included in MarcEdit called MarcCompare (who would've thought) by the late Robert Ellett that can perform a similar function, but the issue with it is that it can't do anything with the files after being compared. The goal we have would be to allow the user to use the barebones MARC file that comes from the CSV to determine if existing, fuller records exist in a master file. Then we could take these and make a new working file for the cataloguers to work with.

The only issue with this functionality would be matching the order for the cataloged books with the record: cataloging at ULS is done basically in whatever order the cataloguer works in. The books come in completely unarranged, but however they exit the cataloguers hands (which should be the same as how they were entered into the file) is the same order the processors have to follow, presumably for the sake of efficiency.

The plan right now would be to grab all of the ISBNs from a target file, then compare them to the master file. Record objects do allow you to grab specific fields, so after grabbing one ISBN, we iterate through the entire list for the master file. When we find the record we need, write it to a new one and break the loop, move onto the next record. Easy on paper, we'll see how it works in practice.