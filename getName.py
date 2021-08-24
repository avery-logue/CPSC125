def getName(prompt) :
    name = input("Enter your "+prompt+" (enter '-' if you don't have a "+prompt+"):")
    return name
def printName(name):
    if (name != '-'):
        print(name, end='')
        
fName = getName('first name')
mName = getName('middle name')
lName = getName('last name')
title = getName('title')
suffix = getName('suffix')

print('Your name is ',end='')

printName(title + " ")
printName(fName + " ")
printName(mName + " ")
printName(lName + " ")
printName(suffix)
print('.')
