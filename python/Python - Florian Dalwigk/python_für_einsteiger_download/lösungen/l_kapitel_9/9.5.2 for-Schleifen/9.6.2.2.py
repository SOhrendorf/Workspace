zahlen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
"""
Das erste Element in der Liste, das ohne Rest durch 3 teilbar ist, ist die 3 mit dem Index 2.
Die Funktion range erhält als Startwert also 2 und als Endwert 15.
Die Schrittweite ist 3, weil jede dritte Zahl durch 3 teilbar ist.
"""
for i in range(2,15,3):
  print(zahlen[i])