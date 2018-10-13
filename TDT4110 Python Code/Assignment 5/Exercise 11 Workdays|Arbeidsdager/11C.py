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
    day=0                       #The variable "day" represents the days in number format. Mon = 0, Thu = 1, etc.So day+=1 means going over to the next day
    for x in range (1900,year+1):
        start_day=day
        if is_leap_year(x):     #leap years have one extra day which means we will add an extra day if this if: statement is True. 
            day+=1
        day+=1
    return (start_day%7)         #We use modula here because when the variable hits the value 7 (7%7 or 14%7 etc), then
                                #the variable%7 will always end up with a number between 0-6. Also it will go as 0,1,2,3,4,5,6 -> 0,1,2, ...


#Checks if the day is a workday or not, not dependent on anything
def is_workday(day):
    if day<=4:                  #0-4 means Monday-Friday. So if "day" is before Friday, also not saturday and sunday, then its a workday
        return True 
    else:
        return False


#Checks the number of workdays in any year after 1900. Dependent on is_leap_year(), is_workday() and weekday_newyear()
def workday_in_year(year):
    for x in range (1900,year+1):
        start_day=weekday_newyear(x)                          #Chooses the correct startday for the starting of each new year
        nr_workdays=0
        if is_leap_year(x):                                   #If its a leap year, then there's 366 days that year. If not than we have 365 days as usual
            day_per_year=366
        else:
            day_per_year=365
        for y in range(start_day,start_day+day_per_year):      #Amount of days per year will stay the same, but it will start from the correct startday
            if is_workday(y%7):                               #and with modula we will be able to end at the correct day too.
                nr_workdays+=1                              
    return nr_workdays                             


#Main function, Dependent on all the functions above to work
def main(year): 
    for x in range (1900,year):
        print("{0}: {1} arbeidsdager".format(x, workday_in_year(x)))
#main(1920)         #Exercise asked for workdays from 1900 to 1919, uncomment #main(1920) to see the answer to this exercise
end_year=int(input("Print out the amount of workdays from 1900 to : "))
main(end_year+1) 


