# Benutzereingaben abfragen.
pi = input("Wie lautet die Kreiszahl PI? ")

# Anzahl der Nachkommastellen.
nachkommastellen = len(pi) - 2 # 2 wird wegen des Vorkommateils (3) und des Punktes (.) abgezogen.

# Ausgabe.
print(f"Du hast {nachkommastellen} Nachkommastellen von PI eingegeben.")
