zahl = 111
if zahl % 5 == 2:       # 111 % 5 = 1
  zahl = 112
elif zahl % 11 == 0:    # 111 % 11 = 1
  zahl = 113
elif zahl % 3 == 0:     # 111 % 3 = 0, d. h. der nachfolgende Code wird ausgeführt.
  zahl = 114            # Der Wert der Variable "zahl" ist jetzt 114.
else:
  zahl = 115
print(zahl)             # Es wird 114 ausgegeben.
