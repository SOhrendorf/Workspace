import random

if __name__ == "__main__":
  lotto = set()
  
  while len(lotto) != 6:
    lotto.add(random.randint(1,49))
  superzahl = random.randint(0,9)
  print(f"Die Lottozahlen: {lotto}\nSuperzahl: {superzahl}")