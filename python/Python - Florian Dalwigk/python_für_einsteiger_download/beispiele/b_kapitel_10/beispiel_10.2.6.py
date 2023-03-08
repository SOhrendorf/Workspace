passwörter =[]
f = open("passwörter.txt", "r+")
passwörter = f.read().splitlines()
print(passwörter)
f.write("h4ck3R")
f.close()