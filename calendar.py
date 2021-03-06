year = int(input("Enter a year: "))

#
# Write your code here.
#
if(year>1582):
    if(year%4==0):
        if(year%100!=0):print("Leap year")
        elif(year%400==0):print("Leap year")
        else: print("Common Year")
    else: print("Common Year")
else: print("Not within the Gregorian calendar period")
