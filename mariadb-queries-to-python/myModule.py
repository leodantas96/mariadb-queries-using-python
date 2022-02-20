# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
# *************************************************************** START BLOCK

import os
import sys
from datetime import datetime
from tabulate import tabulate

def printString( functionName , stringToPrint ):


     myString = "[" + getDateTime() + "]" + functionName + " " + stringToPrint
     print (myString)
# *************************************************************** END BLOCK



# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
def printSplash():

     _function_name = "[fn]" + "[printSplash]"

     os.system('cls' if os.name == 'nt' else 'clear')


     print ( "\n\n" )
     printString (
_function_name,"***********************************************************************"
)
     printString ( _function_name,"system version is : " + sys.version )
     nowDateTime = getDateTime()
     printString ( _function_name,"date and time is :" + nowDateTime )
     printString (
_function_name,"***********************************************************************"
)
     print ( "\n\n" )
     print ("                           Trabalho feito por: -Leonardo e Miguel :D")
     print ( "\n\n" )
     


# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
def getDateTime():
     now = datetime.now()  # current date and time
     date_time = now.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
     return date_time

# print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
# *************************************************************** START BLOCK
def getNowDate():
     myDate = datetime.today().strftime('%Y-%m-%d')
     return myDate