# Avery Logue
# 12/3/17

word = ""
filename = input('Please enter a filename or X to exit\n')

while(word != "X" and filename != "X"): 
    try:
        with open(filename, "r") as infile:
            list = infile.read()
        list = list.split()
        
        while (word != "X"):
            word = input('Please enter a word or X to exit\n')
            if(word == "X"):
                quit
            elif word in list:
                print(word + " is in " + filename)
            elif word not in list:
                print(word + " is not in " + filename)

    except FileNotFoundError:
        print ("File cannot be found.")
        filename = input('Please enter a filename or X to exit\n')
    
