import sys
try:
  # Es wird versucht, den String "2 + 3" in einen Integer umzuwandeln.
  int("2 + 3")
# Es wird jede auftretende Exception abgefangen.
except:
  # Es wird der Name der Klasse ausgelesen, der für die Exception verantwortlich ist.
  error = sys.exc_info()[0]
  # Der Name der Klasse wird anschließend ausgegeben.
  print(f"Es ist ein {error} aufgetreten!")
# Der else-Block wird nie erreicht, weil int("2 + 3") immer zu einem ValueError führt.
else:
  print("Das Programm enthält keine Fehler!")
  
# Die Ausgabe lautet: "Es ist ein <class 'ValueError'> aufgetreten!"