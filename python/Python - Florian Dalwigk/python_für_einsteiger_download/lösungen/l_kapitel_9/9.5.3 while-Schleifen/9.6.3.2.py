ausgaben = [12.50, 13.99, 21.75, 3.14, 13,37]
i = 0
while True:
  if i == len(ausgaben):    
    break
  print(ausgaben[i])
  i += 1

# Als for-Schleife:
for ausgabe in ausgaben:
  print(ausgabe)