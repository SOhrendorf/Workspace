class Pokemon: 
  def __init__(self,name,nr,größe,gewicht,trainer,typ):
    print(f"{name}, {name}!")
    self.__name = name
    self.__nr = nr
    self.__größe = größe
    self.__gewicht = gewicht
    self.__trainer = trainer
    self.__typ = typ
    self.__lebenspunkte = 20

  def einstecken(self, schaden):
    self.__lebenspunkte -= schaden

  def angreifen(self, gegner, schaden):
    gegner.einstecken(schaden)
    
  def get_lebenspunkte(self):
    return self.__lebenspunkte

schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")

schiggy.angreifen(pikachu,5)
print(pikachu.get_lebenspunkte())   # Ausgabe: 15
pikachu.angreifen(schiggy,3)
print(schiggy.get_lebenspunkte())   # Ausgabe: 17