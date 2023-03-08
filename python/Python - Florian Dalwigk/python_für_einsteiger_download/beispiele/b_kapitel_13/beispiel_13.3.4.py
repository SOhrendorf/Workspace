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

pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
print(pikachu.get_gewicht ())   # Ausgabe: 6