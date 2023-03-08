lebensmittel = []
f = open("einkauf.txt", "r")
lebensmittel = f.readlines()
f.close()
print(lebensmittel)
# Ausgabe: ['Tomaten\n', 'Käse\n', 'Nudeln']