class Pokemon: 
  def __init__(self,name,nr,größe,gewicht,trainer,typ):
    print(f"{name}, {name}!")
    self.__name = name
    self.__nr = nr
    self.__größe = größe
    self.__gewicht = gewicht
    self.__trainer = trainer
    self.__typ = typ
    
  def get_gewicht(self):
    return self.__gewicht

  def zunehmen(self, zunahme):
    self.__gewicht += zunahme

  def abnehmen(self, abnahme):
    self.__gewicht -= abnahme
    
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
print(schiggy.get_gewicht())    # Ausgabe: 9
schiggy.zunehmen(3)
print(schiggy.get_gewicht())    # Ausgabe: 12
schiggy.abnehmen(4)
print(schiggy.get_gewicht())    # Ausgabe: 8