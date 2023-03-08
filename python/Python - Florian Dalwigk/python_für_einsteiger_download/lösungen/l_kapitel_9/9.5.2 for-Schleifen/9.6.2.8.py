x = 0
# Der folgende Code wird fünfmal durchlaufen.
for i in range(5):
  # In jedem Schritt wird x um 1 erhöht.
  x += 1
  # Zuerst wird 1, dann 2, dann 3, dann 4 und dann 5 mal ein "!" ausgegeben.
  for j in range(x):
    print("!")
# Insgesamt werden also 1+2+3+4+5=15 Ausrufezeichen ausgegeben.