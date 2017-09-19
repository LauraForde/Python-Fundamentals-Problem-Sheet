# Exercise 2 for the Python Fundamentals work sheet
# Print the current date and time to the screen

# Adapted from https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/

from datetime import datetime

#Obtaining the current date and time
dt = datetime.now()

#Printing the current date and time on seperate lines
print(dt.strftime("The date is: %d-%m-%Y \nThe time is: %H:%M:%S"))
