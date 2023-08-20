import time

# epoch = a date and time from which a computer measures system time
print(time.time()) #returns current seconds since epoch
print(time.ctime(0)) # convert a time expressed in seconds since  epoch to a readable string
print(time.ctime(1000000))
print(time.ctime(time.time())) #prints todays date and time


time_object = time.localtime()
print(time_object)
#time_object = time.gmtime()
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)


time_string = "16 August, 2023"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)



# converting tuple format time to readable
# (year, month, day, hours, minutes, secs, day of the week, day of the year, day light saving)
time_tuple = (2023, 8, 19, 21, 0, 0, 7, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple1 = (2023, 8, 19, 21, 0, 0, 7, 0, 0)
time_string1 = time.mktime(time_tuple)
print(time_string1)