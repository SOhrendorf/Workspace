class Pokemon: 
  def __init__(self,name,nr,größe,gewicht,trainer,typ):
    print(f"{name}, {name}!")
    self.name = name
    self.nr = nr
    self.größe = größe
    self.gewicht = gewicht
    self.trainer = trainer
    self.typ = typ
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
# Ausgabe: Schiggy, Schiggy!