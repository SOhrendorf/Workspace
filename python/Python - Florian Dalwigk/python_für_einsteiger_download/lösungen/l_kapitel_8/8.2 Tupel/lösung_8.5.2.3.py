tupel = (0,1,2,3,3,0)   
kopie = tupel           # (0,1,2,3,3,0) -> Hier wird eine Kopie des Tupels angefertigt. 
print(tupel[2])         # 2
print(kopie[5])         # 0
print(tupel.index(0))   # 0 -> Es wird die Position der ersten 0 ausgegeben.
index = tupel.index(3)  # index = 3
print(kopie[index])     # 3 -> Hier wird auf kopie[3] zugegriffen, weil index = 3 ist.
index = kopie.count(3)  # index = 2, weil die 3 zweimal in dem Tupel vorkommt. 
print(tupel[index])     # 2 -> Hier wird auf tupel[2] zugegriffen, weil index = 2 ist.
print(5 in kopie)       # False -> 5 ist nicht im Tupel enthalten.

"""
Die Ausgabe lautet also:
2
0
0
3
2
False
"""