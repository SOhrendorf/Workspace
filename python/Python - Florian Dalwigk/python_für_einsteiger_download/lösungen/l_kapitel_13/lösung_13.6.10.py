class Tier:
  def __init__(self,name):
    self.name = name
    self.tierart = "Tier"
  
  def __str__(self):
    return f"{self.name} ist ein {self.tierart}."
    
  def reden(self):
    print("...")

class Hund(Tier):
  def __init__(self,name):
    self.name = name
    self.tierart = "Hund"
    
  def reden(self):
    print("Wuff, wuff!")

class Ente(Tier):
  pass
  
class Robbe(Tier):
  def __init__(self,name):
    super().__init__(name)
    self.tierart = "Robbe"
    
  def reden(self):
    print("Ow, ow!")
    
benni = Tier("Benni")
maya = Hund("Maya")
robin = Robbe("Robin")
darkwing = Ente("Darkwing")

print(benni)        # Benni ist ein Tier.
print(maya)         # Maya ist ein Hund.
print(robin)        # Robin ist ein Robbe.
print(darkwing)     # Darkwing ist ein Tier.
benni.reden()       # ...
robin.reden()       # Ow, ow!
darkwing.reden()    # ...
maya.reden()        # Wuff, wuff!