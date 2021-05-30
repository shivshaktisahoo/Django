# 1: dir()

print(dir())       # short for 'directory'

# this is the o/p and displays list of objects when we start interpeter
"""['__annotations__', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__']
"""
# 1.1: __bulitins__ # its a module
print(dir(__builtins__))

# lets use pow function in __bulitins__ module
# help(pow)   # works in terminal not in VSCode(use mouse cursor in function it automatically show)
print(pow(2,10))                # o/p-> 1024

# help(hex)
print(hex(10))                  # o/p-> 0xa
print(0xa)                      # o/p-> 10 (hexadecimalstarts with '0x...' to decimal)

# 1.2:
# show all modules
# print(help('modules'))

# To use modules we have to import that module to directory 
import math
print(dir())  # check their is math module in the directory
"""
['__annotations__', '__builtins__', '__cached__',
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math']
"""

# check what inside math module
print(dir(math))

# print(help(radians))  # NameError: name 'radians' is not defined
# As radians live inside math module so we have give path in this way help(math.radians)
help(math.radians)

# print(radians(180)) # shows an error reason is same "path is not given"
print(math.radians(180))        #o/p: 3.141592653589793

import datetime
# help(datetime.date)

#create date object
gvr = datetime.date(1956, 1, 31) # gvr is Guido van Rossum (creator of python) birth date
print(gvr)          # 1956-01-31
# accessing year, month, day from date object(gvr)
print(gvr.year)     # 1956
print(gvr.month)    # 1
print(gvr.day)      # 31

print(dir(datetime))
# timedelta
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)            # 100 days is incremented

# default Format: YYYY-mm-dd
print(gvr)      # 1956-01-31
# to change default format to different format we have to use format code %A,%B....
# Day-name, month-name, day-#, Year
# strftime is the old method
print(gvr.strftime("%A, %B %d,%Y"))         # Tuesday, January 31,1956
message = "GVR was born on {:%A, %B %d,%Y}"
print(message.format(gvr))

# spaceX resued first stage Rocket:
# March 30, 2017 22:27 UTC
print(dir(datetime))
# we have class date ,time, and datetime

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)      # 2017-03-30
print(launch_time)      # 20:27:00
print(launch_datetime)  # 2017-03-30 22:27:00

# we can access year, month, day, hour min, sec from datetime object(launch_datetime)
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)  
print(launch_datetime.minute)
print(launch_datetime.second)

# Access Current datetime
# Module: datetime
# Class: datetime
# Method: today()
now = datetime.datetime.today()     # Module.Class.method()
print(now)              # 2021-05-25 16:03:13.787057
print(now.microsecond)  # 787057 is micro second  

# Convert Strings to datetimes
# Module: datetime
# Class: datetime
# Method: strptime()
moon_landing = "7/20/1969"      
# converting string to datetime object
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)        # 1969-07-20 00:00:00  as it is now datetime object not a string 
print(type(moon_landing_datetime))  # <class 'datetime.datetime'>

