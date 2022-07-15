def is_leap_year(year):
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year=int(input("Please enter any year of your choice:\n"))               

if is_leap_year(year):
    print(str(year) + " is a leap year.")
    print("It contains 366 days")
else:
    print(str(year) + " is not a leap year")
    print("It contains 365 days")    
