import os
"""
This class contains functions used in the other classes.
"""

"""
Clears the screen after asking the user to press enter.
"""
def clear(skip=False):
    if skip==False or None:
        input("Press enter to continue.")
    os.system('cls' if os.name == 'nt' else 'clear')
    #thanks, https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    pass

"""
Requests an input and ensures it's a positive integer. Returns said integer.
Basically just the input() funciton but with validation built in.
"""
def validate():

    try:
        value = int(input("GIMME NUMBER: "))

    except:
        print("THAT WASN'T A POSITIVE INTEGER.")
        return False

    if(value <= 0):
        print("NUMBER IS ZERO OR NEGATIVE.")
        return False

    else:
        return value
    

"""
Essentially the same thing as validate, but for strings. Is used to get a one letter string for picking subfields for Marc.
"""
def validateSubField():
    try:
        sub = str(input("GIMME LETTER: "))
    except:
        print("If you're reading this, you somehow threw an exception.")
        return False
    if sub.isalpha()==False:
        print("NOT A LETTER.")
        return False
    elif len(sub)==1:
        return sub
    else:
        print("TOO LONG OR SHORT")
        return False
    

"""
Takes a value and checks if its within the range of values. Used in menus.
Note: the range is inclusive, i.e., if you specify a floor of 1, ceiling of 4, 1 and 4 will be valid.

Args:
floor -- The lower value not to be below.
ceil -- The higher value not to be exceeded.
val -- The number being tested.

Returns:
True -- If the value doesn't break the range.
False -- If the value does break the range.
"""
def within(floor, ceil, val):

    try:
        test = int(val)
    except:
        print("Oops, that probably wasn't a numnber.")
        return False
    if test < floor:
        print("Oops, the number was less than "+str(floor)+".")
        return False
    elif test > ceil:
        print("Oops, the number was higher than "+str(ceil)+".")
        return False
    else:
        return True

def peck():
    peck = """
            PPPPPPPPPPP    EEEEEEEEEE      CCCCCCC   KK       KK
            PPP      PP    EE            CC          KK     KKK 
            PPP      PPP   EE           C            KK   KKKK  
            PPP       PP   EE          CC            KKKKKKK    
            PPPPPPPPPPP    EEEEEEEEEE  C             KKKK       
            PP             EE          CC            KKKK       
            PP             EE           CCC          KK KKKK    
            PP             EE             CCCCC      KK    KKKK 
            PP             EEEEEEEEEE      CCCCCCCC  KK       KK
            """
    print(peck)
    
def joke():
    joke = """
                       +                                    
                       ++                                   
                       +++                   ((((((         
                         +++                  ))))))        
                       +++  +++++            ((((((         
                 +++++++         ++++ +       ))))))        
              ++++                     +++++                
            ++                  **         ++++             
           ++   *    * |+         *****       +++           
          ++ ***       ++|                      +++         
         ++  *        ++++||              ***    +++        
         +     +      +|| ++||           +         +        
        ++    ++    |++    ++++||         +        *+       
       ++     +    +++|       +++++|      ++       **+      
      ++    +++ +++######         #####+||  +    -* **+     
    +++  +++|++++ ~~~~~~~~        ~~~~~~~+++++ |   +|++++++ 
 ++++++++++|+   ~~     $$$       ~   $$$  ~ +++|   ++       
       ++*|||  ~       $$$           $$$   ~  ++|   ++      
       +|||||  ~       $$$   .       $$$    ~ ++|||| ++     
      ++|||||| ~       $$$           $$$    ~ ++|||||+++    
    ++++||||| ..::./     .  |  .      :.:::/:++|||||++++++++
+++++++++||||  .::::   .   ||    .   ::::./ ++|||||||       
       ++||||@    .                   .   ++|||||||||       
      +++|||||@                          ++++++|||||+       
      ++|||||||@@@        _______       ++++ +|||||||+      
    ++++||||||||||@@@@                    @@@+||||||||+     
    +++||||||||||||||@@@@              @@@||||||||||||+     
    +++||||||||||||||||||@@###   ####@|||||||||||||||++     
     ++|||||||||||||||||||@@       @@@|||||||||||||||++     
     +++|||||||||||||######@       @#######|||||||||||+     
      ++||||||#################################+|||+++      
  BEEP+++|||||###################################++++BEEP   
    """
    print(joke)
    #"raughs"
    return
    