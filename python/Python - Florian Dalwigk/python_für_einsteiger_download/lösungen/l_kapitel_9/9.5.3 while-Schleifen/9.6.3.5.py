gerade = []
zahl = int(input("Gib eine gerade Zahl ein: "))
while zahl % 2 == 0:
  gerade.append(zahl)
  zahl = int(input("Gib eine gerade Zahl ein: "))
print(gerade)

# Mit Walross-Operator.
while (zahl := int(input("Gib eine gerade Zahl ein: "))) % 2 == 0:
  gerade.append(zahl)
print(gerade)