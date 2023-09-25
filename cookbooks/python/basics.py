# All of the basics are here if a review is needed

# You can import an entire library with just import or use ' from * import * ' to use specific parts of the library
# then you can use ' as ' keyword to rename it locally
from datetime import datetime as date

# Use pass if you need to run/test code while other class/function has yet to be written
class YetToBeWrittenClass:
    pass

class CookieCutter:

    # Class attributes are basically local variables that may not require user input and can be set before object initialization
    clinic_name = "McNowhere Hospital"
    checkIn = str(date.now())

    # The init function is for passing arguments when the class is instantiated
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    

# Put the class name into the parentheses to extend Parent class to Child class
class ChildOfCookieCutter(CookieCutter):
    pass
    


# This is just to instantiate the above code

checkUp = CookieCutter("Janice", 300)
checkUp2 = CookieCutter("Steve", 150)
print(checkUp.clinic_name)
print(checkUp.date)
print(checkUp.name)
print(checkUp2.name)
print(checkUp.weight)
print(checkUp2.weight)