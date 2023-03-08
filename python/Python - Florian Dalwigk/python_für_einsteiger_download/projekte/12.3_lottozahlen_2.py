import random

if __name__ == "__main__":
  lotto = random.sample(range(1,50), 6)
  superzahl = random.randint(0,9)
  print(f"Die Lottozahlen: {lotto}\nSuperzahl: {superzahl}")