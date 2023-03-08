class OutOfBoundsError(Exception):
  def __init__(self,wert,msg="Wert außerhalb der Grenzen!"):
    self.wert = wert
    self.msg = msg

  def __str__(self):
    return f"{self.wert} -> {self.msg}"

class ValueTooSmallError(OutOfBoundsError):
  def __str__(self):
    return f"{self.wert} -> Der Wert ist zu klein!"

class ValueTooBigError(OutOfBoundsError):
  def __str__(self):
    return f"{self.wert} -> Der Wert ist zu groß!"

if __name__ == "__main__":
  untergrenze = 1
  obergrenze = 10

  zahl = int(input("Gib eine Zahl zwischen 1 und 10 ein: "))
  
  if zahl < untergrenze or zahl > obergrenze:
    raise OutOfBoundsError(zahl)
  else:
    print(f"Deine Zahl ist {zahl}!")