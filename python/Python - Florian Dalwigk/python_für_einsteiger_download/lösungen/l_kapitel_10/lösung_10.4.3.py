# Da der Modus r+ ausgewählt wurde, kann die Datei gelesen UND beschrieben werden.
# Es fehlt allerdings die Angabe eines Filehandles, der ab Zeile 2 aber genutzt wird.
# Ergänze also mit dem Keyword "as" den Filehandle "zutaten".
with open("zutaten.txt", "r+") as zutaten:

# In Zeile 2 und 3 befindet sich kein Fehler.
  zutaten.write("Butter\n")
  zutaten.write("Zucker\n")
  
# Zeile 4 muss entfernt werden, da der Kontextmanager genutzt wird und deshalb kein Aufruf von close erforderlich ist.