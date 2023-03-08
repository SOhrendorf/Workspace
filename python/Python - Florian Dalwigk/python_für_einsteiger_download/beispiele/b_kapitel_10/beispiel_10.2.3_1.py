geburtstagsliste = []
geburtstage = open("geburtstage.txt", "r")
for geburtstag in geburtstage:
  geburtstagsliste.append(geburtstag)
print(geburtstagsliste)
# Ausgabe: ['Shinichi Kudo - 04.05.1994\n', 'Haruka Nanase - 30.06.2000\n', 'Florian Dalwigk - 28.09.1992']
geburtstage.close()