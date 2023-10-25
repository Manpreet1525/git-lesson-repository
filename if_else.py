a=10
b=50
c=100
d=input("enter a number")
d=int(d)
if(d>10 and d<50):
    print(d,"\nEntered number is between 10 to 50")
elif(d>50 and d<100):
    print(d,"\nEntered number is in between 50 to 100")
elif(d<10):
    print(d, "\nEntered Number is less than 10")
else:
    print(d, "\nEntered number is greater than 100")
