import random
# Hauptprogramm.
if __name__ == "__main__":
  # Set für die Lottozahlen erstellen. Ein set wird gewählt, um Duplikate zu verhindern. 
  lotto = set()
  # Solange noch nicht 6 Zahlen (ohne Duplikate) gezogen wurden, 
  while len(lotto) != 6:
    # wird eine Zufallszahl von 1 bis 49 gezogen.
    lotto.add(random.randint(1,49))
  # Zum Schluss wird eine Superzahl von 0 bis 9 gezogen.
  superzahl = random.randint(0,9)
  # Die Lottozahlen werden ausgegeben.
  print(f"Die Lottozahlen: {lotto}\nSuperzahl: {superzahl}")