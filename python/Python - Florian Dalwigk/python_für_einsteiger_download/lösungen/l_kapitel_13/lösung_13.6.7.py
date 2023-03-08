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

  def get_lebenspunkte(self):
    return self.__lebenspunkte

  # Lebenspunkte erhöhen.
  def lebenspunkte_erhöhen(self, punkte):
    self.__lebenspunkte += punkte
    
  # Lebenspunkte verringern.
  def lebenspunkte_verringern(self, punkte):
    self.__lebenspunkte -= punkte
  
  # Lebenspunkte übertragen.
  def lebenspunkte_übertragen(self, pokemon, punkte):
    # Prüfen, ob die Lebenspunkte übertragen werden können.
    if self.__lebenspunkte - punkte >= 1:
      # Lebenspunkte abziehen. 
      self.lebenspunkte_verringern(punkte)
      # Lebenspunkte an das Pokémon übertragen.
      pokemon.lebenspunkte_erhöhen(punkte)
    else:
      print("Die Lebenspunkte können nicht übertragen werden!")

# Beispielprogramm
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
schiggy.lebenspunkte_übertragen(pikachu,5)
print(schiggy.get_lebenspunkte())
print(pikachu.get_lebenspunkte())