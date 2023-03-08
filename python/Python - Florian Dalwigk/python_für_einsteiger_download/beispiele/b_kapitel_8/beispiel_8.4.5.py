obstsorten = {
  "Banane" : 8,
  "Erdbeere" : 10,
  "Weintraube" : 9, 
  "Kiwi" : 3
}
bewertung_erdbeere = obstsorten["Erdbeere"]
erdbeerpunkte = obstsorten.get("Erdbeere")
print(erdbeerpunkte == erdbeerpunkte)
# Ausgabe: True
print(obstsorten.get("Blaubeere"))
# Ausgabe: None