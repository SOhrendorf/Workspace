import random
# Hauptprogramm.
if __name__ == "__main__":
  # Mithilfe der Funktion sample auf random werden 6 Zufallszahlen (ohne Duplikate) gezogen.
  lotto = random.sample(range(1,50), 6)
  # Zum Schluss wird eine Superzahl von 0 bis 9 gezogen.
  superzahl = random.randint(0,9)
  # Die Lottozahlen werden ausgegeben.
  print(f"Die Lottozahlen: {lotto}\nSuperzahl: {superzahl}")