zahlen = [10,11,12,13,14,15,16,17,18,19,20]
"""
Beachte, dass 10 das erste Element der Liste mit dem Index 0 ist.
Die Funktion range erhält als Startwert also 0 und als Endwert 10.
Die Schrittweite ist 2, weil wir nur die geraden Zahlen ausgeben wollen.
"""
for i in range(0,11,2):
  print(zahlen[i])