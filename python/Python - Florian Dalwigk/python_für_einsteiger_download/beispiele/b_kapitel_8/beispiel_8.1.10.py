antworten = [True,42,"J","N",3.0][2:4]
print(antworten)
# Die Ausgabe lautet ["J","N"]
liste = [True,42,"J","N",3.0]
print(liste[2:3])
# Die Ausgabe lautet ["J","N"]

# Die folgenden beiden Listen sind gleich
variante1 = [True,42,"J","N",3.0][0:4]
variante2 = [True,42,"J","N",3.0][4]
print(variante1 == variante2)

# Du kannst die gesamte Liste auf zwei verschiedene Arten auslesen:
variante1 = True,42,"J","N",3.0][0:5]
variante2 = [True,42,"J","N",3.0][:]
print(variante1 == variante2)