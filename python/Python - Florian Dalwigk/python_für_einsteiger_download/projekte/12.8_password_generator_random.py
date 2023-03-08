import random
import string as s

def passwort_generieren(laenge):
  gross = s.ascii_uppercase
  klein = s.ascii_lowercase
  zahlen = s.digits
  sonderzeichen = s.punctuation
  zeichen = [gross,klein,zahlen,sonderzeichen]
  passwort = [] 
  for x in zeichen:
    passwort.append(random.choice(x))
  zeichensatz = ''.join(zeichen)
  for _ in range(laenge):
    passwort.append(random.choice(zeichensatz))
  random.shuffle(passwort)
  return ''.join(passwort)

if __name__ == "__main__":
  n = int(input("Passwortlänge? "))
  passwort = passwort_generieren(n)
  print(passwort)