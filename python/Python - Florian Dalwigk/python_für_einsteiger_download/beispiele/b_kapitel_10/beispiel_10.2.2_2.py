lebensmittel = []
f = open("einkauf.txt", "r")
lebensmittel = f.read().splitlines()
f.close()
print(lebensmittel)
# Ausgabe: ['Tomaten', 'Käse', 'Nudeln']