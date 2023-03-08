class Pokemon:
  def __init__(self,name,nr,größe,gewicht,trainer):
    self.__name = name
    self.__nr = nr
    self.__größe = größe
    self.__gewicht = gewicht
    self.__trainer = trainer
    self.__lebenspunkte = 20
    self.__typ = "Pokémon"

  def get_name(self):
    return self.__name

  def get_nr(self):
    return self.__nr

  def get_größe(self):
    return self.__größe
    
  def get_gewicht(self):
    return self.__gewicht
    
  def get_trainer(self):
    return self.__trainer

  def get_typ(self):
    return self.__typ
    
  def get_lebenspunkte(self):
    return self.__lebenspunkte

  def einstecken(self, schaden):
    self.__lebenspunkte -= schaden

  def angreifen(self, gegner, schaden):
    gegner.einstecken(schaden)

class Wasserpokemon(Pokemon):
  def get_typ(self):
    return "Wasserpokémon"

  def angreifen(self,gegner,schaden):
    print("Wasserattacke!")
    super().angreifen(gegner,schaden)

class Feuerpokemon(Pokemon):
  def get_typ(self):
    return "Feuerpokémon"
    
  def angreifen(self,gegner,schaden):
    print("Feuerattacke!")
    super().angreifen(gegner,schaden)

class Elektropokemon(Pokemon):
  def get_typ(self):
    return "Elektropokémon"
    
  def angreifen(self,gegner,schaden):
    print("Elektroattacke!")
    super().angreifen(gegner,schaden)

if __name__ == "__main__":
  schiggy = Wasserpokemon("Schiggy",7,0.5,9,"Misty")
  glumanda = Feuerpokemon("Glumanda",7,0.6,8.5,"Ash")
  schiggy.angreifen(glumanda,7)
  print(glumanda.get_lebenspunkte())