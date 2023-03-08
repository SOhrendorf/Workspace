passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper())        # "ABC123"
print(passwort2.lower())        # "pass wort"
print(passwort3.islower())      # True, weil alle Zeichen "klein" sind.
print(passwort2.isupper())      # False, weil nicht alle Zeichen "groß" sind.
print(passwort1.zfill(8))       # "00abc123". Es werden zwei Nullen ergänzt, weil eine 8 in zfill steht und "abc123" 6 Zeichen hat.
print(passwort2.strip())        # "Pass Wort". Das Leerzeichen wird nicht entfernt, weil es nicht am Anfang/Ende steht.
print(len(passwort3))           # 12, weil "u1tr4g3h31m " 12 Zeichen hat (Leerzeichen mitzählen!)