#Avery Logue 10/25/17
def getGrade(nbr) :
    if(int(nbr) >= 90 and int(nbr) < 100):
        return 'A'
    elif(int(nbr) >= 80 and int(nbr) < 90):
        return 'B'
    elif(int(nbr) >= 70 and int(nbr) < 80):
        return'C'
    elif(int(nbr) >= 60 and int(nbr) < 70):
        return'D'
    else :
         return 'F'

print("Enter your grade: ")
b = getGrade(input())
print("Your grade is: "+ b)
