class Zahl:
  def __init__(self, wert):
    self.wert = wert
    
try:
  wert = int(input("Geben Sie einen Wert an: "))
  zahl = Zahl(wert)
  ergebnis = 42 / zahl.wert
# Auf den try-Block folgt der finally-Block.
finally: 
  """
  Wenn der Benutzer etwas eingibt, das KEINE Zahl ist (z.B. "3,o1"), 
  dann wird das Zahl-Objekt gar nicht erst erzeugt und es kommt
  bei der Lösch-Anweisung zu einer NameError Exception, die mit einer 
  try-catch-Anweisung abgefangen werden kann.
  """
  try:
    del zahl
  except NameError:
    print("Das Objekt konnte nicht gelöscht werden, weil es nicht existiert!")
  # Wenn keine NameError Exception geworfen wird, kann die Löschmeldung ausgegeben werden.
  else:
    # Die Meldung über das erfolgreiche Löschen wird ausgegeben.
    print("Das Zahl-Objekt wurde gelöscht!")

