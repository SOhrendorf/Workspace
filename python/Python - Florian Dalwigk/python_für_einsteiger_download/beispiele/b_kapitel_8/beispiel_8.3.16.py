bits = {0,1}
import itertools
produkt = itertools.product(bits,repeat=2)
print(list(produkt))
# Ausgabe: [(0, 0), (0, 1), (1, 0), (1, 1)]