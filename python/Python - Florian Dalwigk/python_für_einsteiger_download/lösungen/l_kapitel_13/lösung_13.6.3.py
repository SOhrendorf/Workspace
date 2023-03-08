class Pokemon:
  def __init__(self,name,nr,größe,gewicht,trainer,typ):
    self.__name = name
    self.__nr = nr
    self.__größe = größe
    self.__gewicht = gewicht
    self.__trainer = trainer
    self.__typ = typ
    # Gib den Namen des Pokémons aus, wenn er nicht "Pikachu" ist.
    if name != pikachu:
      print(f"{name}, {name}!")
    else:
      # Spezialfall "Pikachu".
      print("Pika, Pika!")
    
  def __eq__(self,other):
    return self.__name == other.__name