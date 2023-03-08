def rückgabe():
  return True, "Antwort", 42
wahrheitswert,text,zahl = rückgabe()
wahrheitswert,text,zahl,name = rückgabe()
# ValueError: not enough values to unpack (expected 4, got 3)
wahrheitswert,text = rückgabe()
# ValueError: too many values to unpack (expected 2)