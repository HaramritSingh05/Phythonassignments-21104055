year_ok = False

while  ( year_ok==False ) :
    year = int(input("Enter  year -"))
    if (year<=0  ) :
        print("Please input valid year !!!!!!")
    else:
        year_ok = True
leap_year =False
if(year%4==0):
    leap_year =True

month_ok = False
while  ( month_ok==False ) :
    month = int(input("\nEnter month -"))
    if (month<=0 or month>=13  ) :
        print("Please input valid month !!!!!!")
    else:
        month_ok = True

day_30_month = [4,6,9,11]

day_ok = False
while  ( day_ok==False ) :
    day =  int(input("\nEnter day -"))
    if (day<=0 or day>31) :
        print("Please input valid day !!!!!!")
    elif (leap_year==False and month==2 and day>28 ):
        print("\nYear you entered is  not a leap year . \n So February cannot have more than 28 days !!!!! \nPlease enter correct day again ")
    elif (leap_year and  month==2 and day>29 ):
        print("\nYear you entered is a leap year .\nSo February cannot have more than 29 days !!!!! \nPlease enter correct day again ")
    elif(month in day_30_month and day>30):
        print("\nMonth you have entered has not  more than 30 days!!!!! \nPlease enter the valid day ")
    else:
        day_ok = True

if((leap_year and month ==2 and  day==29 ) or (leap_year==False and month ==2 and day==28)):
    next_day = 1
    next_month =month+1
    next_year = year
elif(month in day_30_month and day==30):
    next_day = 1
    next_month = month+1
    next_year = year
elif(month ==12 and day==31):
    next_day = 1
    next_month =1
    next_year = year+1
elif(month not in day_30_month and day==31):
    next_day = 1
    next_month =month+1
    next_year = year
else:
    next_day = day+1
    next_month =month
    next_year = year
if(month<10):
    print("\n\nEntered date is : {}/0{}/{}\n".format(day,month,year))
else:
    print("\n\nEntered date is : {}/{}/{}\n".format(day,month,year))
if(next_month<10):
    print("Next date is : {}/0{}/{}\n".format(next_day,next_month,next_year))
else:
    print("Next date is : {}/{}/{}\n".format(next_day,next_month,next_year))
