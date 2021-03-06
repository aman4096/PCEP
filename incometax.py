income = float(input("Enter the annual income: "))

#
# Write your code here.
#
tax=14839.2
if(income<85528): tax=income*0.18-556.2
else: tax+=(income-85528)*0.32
if(tax<0):tax=0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
