nachnamen = {
  "Maria" : "Huber",
  "Martin": "Lampey",
  "Matthias": "Burk"
}

try: 
  # Der Benutzer gibt einen Vornamen (Schlüssel) an.
  vorname = input("Nach wem suchst du? ")
  # Der Nachname wird mit dem Vornamen als Schlüssel im Dictionary "nachnamen" gesucht.
  # Hier kann es zu einem KeyError kommen, wenn der Schlüssel nicht im Dictionary vorhanden ist.
  nachname = nachnamen[vorname]
  print(f"{vorname} {nachname}")
# Hier wird die KeyError Exception abgefangen.
except KeyError:
  print("Es wurde ein Schlüssel angegeben, der nicht im Dictionary existiert.")