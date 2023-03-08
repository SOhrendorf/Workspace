def addieren_und_multiplizieren(a,b):
  summe = a + b
  produkt = a * b
  return summe,produkt
ergebnis = addieren_und_multiplizieren(5,10)
print(ergebnis)
type(ergebnis) # <class 'tuple'>
summe,produkt = addieren_und_multiplizieren(5,10)
print(f"Summe = {summe}\nProdukt = {produkt}")
"""
Ausgabe: 
--------------------------
Summe = 15
Produkt = 50
"""