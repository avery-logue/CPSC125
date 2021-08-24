def addtwo(val1, val2):
    sum = val1 + val2
    return sum
summ = addtwo(7, 5)
print(summ)

def getNumber() :
    print("Enter a number")
    x = input()
    return x

a = addtwo(int(getNumber()), int (getNumber()))
b = addtwo(int(getNumber()), int (getNumber()))
c = addtwo(int(getNumber()), int (getNumber()))
d = addtwo(int(getNumber()), int (getNumber()))
e = addtwo(int(getNumber()), int (getNumber()))
print(a+b+c+d+e)
