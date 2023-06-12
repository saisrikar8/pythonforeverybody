# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#taking the input of hours as a float
hrs = input("Enter Hours: ")
h = float(hrs)

#taking the input of rate per hour as a float
rate = input("Enter the rate per hour: ")
r = float(rate)

#Getting the pay and printing it
pay = r*h
if h > 40:
    extraHours = h-40
    pay = r*40 + extraHours*r*1.5
print(pay)