def datenabfrage(**daten):
  vorname = daten.get("vorname")
  nachname = daten.get("nachname")
  alter = daten.get("alter")
  print(f"{vorname} {nachname}, {alter}")
datenabfrage(vorname="Mia", nachname="Marbles")
# Ausgabe: Mia Marbles, None