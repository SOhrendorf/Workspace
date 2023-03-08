def multiplizieren(a,b,c):
  produkt = a * b * c
  return produkt
multiplizieren(1,2)     # TypeError: multiplizieren() missing 1 required positional argument: 'c'
multiplizieren(1,2,3,4) # TypeError: multiplizieren() takes 3 positional arguments but 4 were given