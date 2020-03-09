#Ricky Deegan
#this program lets you know if its a weekday or not.
# need to import daytime function.
import datetime

#currentday is the variable created to show present day 
Currentday = datetime.datetime.now( ) 
#0 = Mon, 1 = Tue, etc. If condition with positional index to identify position of current date in the days of week.
if Currentday.weekday ( ) < 5:
    print("Yes its a weekday") #print values 0-4

elif Currentday.weekday ( ) > 4:
    print("Yes its the weekend") # print values 5-6

