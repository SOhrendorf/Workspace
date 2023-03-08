"""
Es werden immer drei aufeinanderfolgende Zahlen in einem 3-Tupel gespeichert.
Die 3-Tupel haben also die Form (x,x+1,x+3).
Das erste 3-Tupel ist (1,2,3), d. h. die range-Funktion erhält als Startwert x=1.
Da das letzte 3-Tupel (16,17,18) ist, lautet der Endwert 17. Der letzte Index ist dann 16.
Da immer drei Zahlen aufeinanderfolgen, ist die Schrittweite 3.
"""
[(x,x+1,x+2) for x in range(1,17,3)]