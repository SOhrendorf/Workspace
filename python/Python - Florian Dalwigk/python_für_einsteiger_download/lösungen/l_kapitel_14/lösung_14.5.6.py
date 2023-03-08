# Wir definieren eine Klasse, die von "Exception" erbt.
class IsNotPrimeError(Exception):
  # In der __init__-Methode wird ein Wert übergeben und einer Objektvariable zugewiesen.
  def __init__(self, wert):
    self.wert = wert
  # Die __str__-Methode wird überschrieben.
  def __str__(self):
    return f"{self.wert} ist keine Primzahl!"

def prim(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True
  
zahl = int(input("Gib eine Primzahl ein: "))

if not prim(zahl):
  raise IsNotPrimeError(zahl)