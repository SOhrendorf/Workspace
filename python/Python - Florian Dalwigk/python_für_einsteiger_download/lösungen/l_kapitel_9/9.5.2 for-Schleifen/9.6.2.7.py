obstsorten = ["Banane","Apfel","Mango","Erdbeere","Melone"]

# Wir gehen nacheinander alle Obstsorten in der Liste durch.
for obstsorte in obstsorten:
  # Wenn die Anzahl der Buchstaben in der Obstsorte nicht 8 ist, ...
  if len(obstsorte) != 8:
    # ... dann wird die Obstsorte ausgegeben.
    print(obstsorte)
  else:
    # Ansonsten wird die Schleife mit einem "break" verlassen.
    break