##Ask to input numbers:using try and error
##How many times user wants to enter numbers
#avg and sum of all the number

# def sum_and_average():
#     No_of_times= int(input("Enter number of times you want to enter number"))
#     for x in range(No_of_times):
#         num=int(input("Enter a number: "))
#         print(num)
#     sum=sum(num)
#     print(sum)
'''exit_condition = False

try:

    <some code ...>

    if exit_conditon is True:
        raise UnboundLocalError('My exit condition was met. Leaving try block')

    <some code ...>

except UnboundLocalError, e:
    print 'Here I got out of try with message %s' % e.message
    pass

except Exception, e:
    print 'Here is my initial exception'

finally:
    print 'Here I do finally only if I want to'''
b=[]  ##Defining Empty list
num= int(input("take number of inputs to be typed by the users: "))
if (num>=2 and num<=5): 
    for i in range(0,num):  
        b.append(int(input('enter number: '))) #add input in a list   
    print("sum of all numbers is",sum(b)) #sum of values in list after while is over
else:
    print("Enter a number between 2 and 5")       
# except ValueError: #to diplay error message if entered number is not in range
#     print("enter a number between 2 and 5")



    

