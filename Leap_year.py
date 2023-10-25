## to check if user input year is a leap or not
year=int(input("Enter a year: "))
if(year%4==0 and year%100!=0):
    print(f"Entered {year} is leap year")
elif(year%400==0):
    print(f"Entered {year} is leap year")
else:
    print(f"Entered year {year} is not a leap year")