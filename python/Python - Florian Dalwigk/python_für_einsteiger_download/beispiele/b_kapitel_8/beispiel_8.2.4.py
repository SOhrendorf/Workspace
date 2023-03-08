def rückgabe():
  return True, "Antwort", 42
ergebnis = rückgabe()
print(type(ergebnis))
# Ausgabe: <class 'tuple'>
print(ergebnis)
# (True, "Antwort", 42)