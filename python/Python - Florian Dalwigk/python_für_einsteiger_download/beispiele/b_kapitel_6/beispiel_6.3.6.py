def datenabfrage(**daten):
  vorname = daten.get("vorname","Max")
  nachname = daten.get("nachname","Mustermann")
  alter = daten.get("alter",18)
  print(f"{vorname} {nachname}, {alter}")
datenabfrage(vorname="Mia", nachname="Marbles")
# Ausgabe: Mia Marbles, 18
datenabfrage()
# Ausgabe: Max Mustermann, 18