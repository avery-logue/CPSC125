def getName(prompt) :
    name = input("Enter your "+prompt+" (enter '-' if you don't have a "+prompt+"):")
    return name
def printName(name):
    if (name != '-'):
        print(name, end='')
def payRate(x):
    print("How many dollars do you make per hour?")
    x = input()
    return x
def hours(y):
    print("How many hours did you work today?")
    y = input()
    return y
def wage(y, x):
    wage = y*x
    return wage

fName = getName('first name')
mName = getName('middle name')
lName = getName('last name')
print('Hello ',end='')

printName(fName + " ")
printName(mName + " ")
printName(lName + " ")

a = payRate(input())
b = hours(input())
q = wage(int(a), int(b))
print("Your gross wage today is: " +str(q)+ "$")
