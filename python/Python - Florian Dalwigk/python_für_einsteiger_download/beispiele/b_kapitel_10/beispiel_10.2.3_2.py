geburtstagsliste = []
geburtstage = open("geburtstage.txt", "r")
for geburtstag in geburtstage:
  geburtstagsliste.append(geburtstag.strip())
print(geburtstagsliste)
# Ausgabe: ['Shinichi Kudo - 04.05.1994', 'Haruka Nanase - 30.06.2000', 'Florian Dalwigk - 28.09.1992']
geburtstage.close()