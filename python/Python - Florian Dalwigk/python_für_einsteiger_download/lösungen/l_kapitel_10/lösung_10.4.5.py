# Zeile 1 kann unverändert bleiben.
meine_filme = []

# "filme =" wird durch das Keyword "with" ersetzt und der Filehandle mit einem "as" hinter die open-Funktion geschrieben.
with open("filme.txt", "r") as filme:

# Die Zeilen 3 und 4 können unverändert bleiben, müssen aber eingerückt werden.
  for film in filme:
    meine_filme.append(film)

# Ein Schließen der Datei in Zeile 5 ist nicht erforderlich.