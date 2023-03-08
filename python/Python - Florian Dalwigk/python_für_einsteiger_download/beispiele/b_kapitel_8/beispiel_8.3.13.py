primzahlen = {17,37,53,39,11,19}
primzahlen_liste = list(primzahlen)
print(type(primzahlen_liste))
# Ausgabe: <class 'list'>
primzahlen_liste.sort()
print(primzahlen_liste)
kleinste_primzahl = primzahlen_liste[0]
print(f"Die kleinste Primzahl ist: {kleinste_primzahl}.")