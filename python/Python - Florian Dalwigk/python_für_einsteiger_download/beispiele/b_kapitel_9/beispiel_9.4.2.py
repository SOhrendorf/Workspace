zahl = 0
fortfahren = "J"
while fortfahren == "J":
  zahl = zahl + 1
  print(zahl)
  fortfahren = input("Hochzählen? (J/N) ")
print(f"Du hast bis {zahl} gezählt.")