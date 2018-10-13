#Checks if its a leap year
def is_leap_year(year):         
    if year % 400 == 0:
        return True 
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

#Checks which is the first day of each year, function is dependent on the is_leap_year() function to check if the year is a leapyear
def weekday_newyear(year):     
    days_inText=["Monday","Tuesday","Wedensday","Thursday", "Friday", "Saturday", "Sunday"]
    day=0                       #The variable "day" represents the days in number format. Mon = 0, Thu = 1, etc.So day+=1 means going over to the next day
    for x in range (1900,year+1):
        start_day=day
        if is_leap_year(x):     #leap years have one extra day which means we will add an extra day if this if: statement is True. 
            day+=1
        day+=1
        print("{0}: {1}".format((x),days_inText[(start_day%7)]))  
        weekday_newyear(1920)   #Here i use %7 because when start_day hits 7, 14, 21 . Then start_day%7 will become 0
                                #This means it will reset to Monday after a full rotation of 0-6(1 week).
