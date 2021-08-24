#Avery Logue 10/25/17
def getSmall(a, b, c) :    
    if(a < b and a < c) :
        return a
    elif(b < a and b < c) :
        return b
    else:
        return c


print("Enter 3 numbers: ")
x = getSmall(input(), input(), input())
print("The smallest number is: " + x)
