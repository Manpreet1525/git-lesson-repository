##Enter names by the user and store in a list(keys)
##Enter age by the user and store in a list(value)
##diplay like a set in respect to keys and values
numb=int(input("Enter number of times you want user to enter the data"))
names= []
ages= []
dict= {}
i=0
for x in range(numb):
    name=input("Enter names: ")
    age=input("enter age: ")
    names.append(name)
    ages.append(age)
                                                # print(names)
                                                # print(ages)
    while(i<=x):
        dict[(names[i])]= ages[i]
        i+=1
        print(dict)
