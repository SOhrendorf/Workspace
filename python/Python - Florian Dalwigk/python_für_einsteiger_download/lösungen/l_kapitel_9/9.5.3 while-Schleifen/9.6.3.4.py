fortschritt = 0
limit = 100
while fortschritt < limit:
  print(f"Laden ... {fortschritt/limit*100}%")
  fortschritt += 1

# Als do-while-Schleife:
while True:
  print(f"Laden ... {fortschritt/limit*100}%")
  fortschritt += 1
  if not fortschritt < limit:
    break