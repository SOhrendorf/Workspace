namen = ["Kevin","Junus","Flo","Lisa","Laura"]
"""
Wir beginnen beim letzten Element in der Liste, das den Index 4 hat. Das ist der Startwert.
Der Endwert ist -1.
Als Schrittweite wird -1 angegeben, da wir die Liste von hinten nach vorne durchlaufen.
"""
for i in range(4,-1,-1):
  print(namen[i])