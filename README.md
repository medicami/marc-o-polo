# marc-o-polo
A small project to convert Linux datafiles containing bilbiographic data into MaRC files or other usable formats.

The Problem
    When books are received, information about them comes in a datafile on a Linux server. The file itself is essentially unusable for the cataloguers and other staff, who typically do their work on Windows machines. In order to convert this information into a usable formate for the other staff to use, information for individual books is printed out onto receipts and placed inside of the items for future processing.

The Goal
    To find a method of converting these datafiles into a usable format. The theoretical minimum would be to extract the information from the datafiles and export it to a Windows compatible format, such as an Excel spreadsheet, comma separated value .txt file, or whatever. In a perfect world, this information could be used to create template MaRC records, allowing for certain fields to be filled in automatically using information from the datafile.

The Plan
    The practicality of this project hinges on whether or not any common programming languages offer support for the original datafiles. Given that (as of February 2) I haven't heard any response from the client, I am going to proceed with the project in theoretical terms. With some cursory research, there is a Python module called Pymarc, which provides utilities for creating MaRC records using the Python language. If inputting information from the datafile is as easy as this, I am cautiously optimistic about the feasability of this project. If I were to start making the program, I would likely break it down into the following steps:

    Stage 0: Planning, outlining what inputs and outputs will be involved, what functionality to implement, pseudocode, etc.
    Stage 1: Can we read from the datafile at all.
    Stage 2: Try taking the input from the datafile and outputting it into another file format, such as .xlsx, .csv, .txt, etc.
    Stage 3: MaRC, creating a MaRC record using Pymarc based on information from variables in code.
    Stage 4: Taking the input from the datafile, assigning them to the variables, and seeing if it results in a working .marc file.
    Stage 5: Combining the previous steps into a single program that can take one input file and output one output file.
    Stage 6: Make the program more user friendly, ideally not requiring command line/terminal and usable as an executable.
    Stage 7: Make the program pretty with an actual GUI, probably definitely not feasible in the span of the class. This is natively available to code in Python with Tkinter, but looks (with all due respect) like a nightmare.

Any actual code is to be here: https://github.com/medicami/marc-o-polo