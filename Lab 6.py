fileList = []
filename = input('Please enter a filename ')

if (filename == 'X'):
    quit


file = open(filename, "r")

contents = file.read()
file.close()
fileList = contents.spilt(' ')

word = " "
while(word != "X"):
    word = input("Please enter a word or enter X to exit ")
    if(word == "X"):
        quit
    elif(word in fileList):
        print(word, "is in ", file)
    else:
        print(word, "is not in ", file)
