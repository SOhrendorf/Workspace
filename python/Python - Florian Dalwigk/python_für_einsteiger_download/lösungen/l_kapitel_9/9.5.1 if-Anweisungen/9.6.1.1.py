# Benutzernamen einlesen.
name = input("Wie heißt du? ")

# Wir lesen den ersten Buchstaben des Namens aus.
# Da wir die Vokale als Großbuchstaben abfragen, 
# wandeln wir den ausgelesenen Buchstaben direkt in einen Großbuchstaben um.
buchstabe = name[0].upper()

# Wir prüfen, ob sich der Buchstabe in der Liste mit Vokalen befindet.
if buchstabe in ['A','E','I','O','U']:
  # Der Name wird in Großbuchstaben ausgegeben.
  print(name.upper())
else:
  print("Dein Name beginnt nicht mit einem Vokal!")