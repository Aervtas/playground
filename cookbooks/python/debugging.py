# Logging - this needs to go at the top of the file under (#! python) shebang line
# DO NOT USE PRINT TO DEBUG PROGRAMS
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of the program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')

# Logging levels are as follows
# DEBUG       logging.DEBUG
# INFO        logging.INFO
# WARNING     logging.WARNING
# ERROR       logging.ERROR
# CRITICAL    logging.CRITICAL

# disable logging to specified level and below (CRITICAL to stop all logging)
logging.disable(logging.CRITICAL)

# Set logging to a file 'myProgramLog.txt'
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# IDLE has a built in nifty debugger and also allows you to right-click and set a breakpoint in the program

# raising exceptions
# raise Exception("Error Message")

# return traceback as a string
import traceback
try:
    raise Exception("Error Message Here")
except:
    errorFile = open('errorLogs.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written into errorLogs.txt")

# Assertions using assert
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# here we accidentally change the variable that we want to stay the same and it throws an error
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
