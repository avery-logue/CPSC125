##Text adventure!

print("Ay lmao ma boi. You have entered the memey world of internet land. Choose your class")
print("Ranger: Has some shit armor, but a coolio bow and a knife")
print("Knight: Rocking the long sword and neato armor")
#print("Traveler: Best of both worlds, sports medium armor with a short sword")

a = input()
armor = 0
inventory = []
if(a == 'Ranger'):
    inventory = ['bow', 'knife']
    armor = 10
    
if(a == 'Knight'):
    inventory = ['longsword']
    armor = 20
    
print("Great choice picking the " + a + " character")
print("Some tips: type inventory to check your inventory and armor to check you're armor")
print("")
print("")
print("You are approached in a bar by an old man")
print(" (@)   (@)")
print("     \    ")
print("  \______/")
print("")
print("Hey-o, whats the jimmy my man?")
print("Text Options:")
print("1: hot diggity dog my homie. it is wednesday my dude")
print("2: what the hell are you talking about old man?")
print("3: I don't have time for this, go away")

a = input()
if(int(a) == 1):
    print("Old man: wowee kiddo, do i have a questerino for you. go fetch me a fucking burrito from the tutorial fields") quest1 = 1
    print("1: coolio my homie g, brb my manz")
    print("2: yo my dude, i gots to go do something else. smell ya later")
    print("3: imma say it, i dont care that you broke your elbow")
if(a == 2):
    print("well ma boi, you are need an A D V E N T U R E")
if(a == 3):
    print("well, you sure you don't wanna go on a adventure?")
    
