class Pokemon:
  def __init__(self,name,nr,größe,gewicht,trainer,typ):
    self.__name = name
    self.__nr = nr
    self.__größe = größe
    self.__gewicht = gewicht
    self.__trainer = trainer
    self.__typ = typ
  
  def __eq__(self,other):
    return self.__name == other.__name
 
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu1 = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
pikachu2 = pikachu1
pikachu3 = Pokemon("Pikachu", 25, 0.35, 5, "Max", "Elektro")
glumanda = Pokemon("Schiggy", 4, 0.61, 8.5, "Ash", "Feuer")

print(schiggy == pikachu1)      # False, weil die Namen der beiden Pokémon-Objekte unterschiedlich sind.
print(schiggy == schiggy)       # True, weil die Namen der beiden Pokémon-Objekte gleich sind.
print(schiggy is schiggy)       # True, weil die beiden Pokémon-Objekte identisch sind.
print(pikachu1 == pikachu2)     # True, weil die Namen der beiden Pokémon-Objekte gleich sind.
print(pikachu2 is pikachu1)     # True, weil pikachu1 und pikachu2 auf dasselbe Objekt zeigen.
print(glumanda is glumanda)     # True, weil die beiden Pokémon-Objekte identisch sind.
print(glumanda == schiggy)      # True, weil die Namen der beiden Pokémon-Objekte gleich sind.
print(glumanda is schiggy)      # False, weil die beiden Pokémon-Objekte nicht identisch sind.
print(pikachu1 == pikachu3)     # True, weil die Namen der beiden Pokémon-Objekte gleich sind.
print(pikachu1 is pikachu3)     # False, weil die beiden Pokémon-Objekte nicht identisch sind.

# Beachte, dass die __eq__ Methode für den == Operator hier nur die Namen der Pokémon vergleicht.