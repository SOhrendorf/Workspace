class Pokemon: 
  def __init__(self,name,nr,größe,gewicht,trainer,typ):
    print(f"{name}, {name}!")
    self.__name = name
    self.__nr = nr
    self.__größe = größe
    self.__gewicht = gewicht
    self.__trainer = trainer
    self.__typ = typ
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
print(schiggy.trainer)
# AttributeError: 'Pokemon' object has no attribute '__trainer'