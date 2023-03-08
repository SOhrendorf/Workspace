import string as s
import hashlib, random

def hash_berechnen(text):
  sha1_hash = hashlib.sha1(text.encode())
  hex_darstellung = sha1_hash.hexdigest()
  return hex_darstellung

def passwort_generieren(laenge):
  gross = s.ascii_uppercase
  klein = s.ascii_lowercase
  zahlen = s.digits
  sonderzeichen = s.punctuation
  zeichen = [gross,klein,zahlen,sonderzeichen]
  passwort = [] 
  for x in zeichen:
    passwort.append(random.choice(x))
  zeichensatz = "".join(zeichen)
  while len(passwort) < laenge:
    passwort.append(random.choice(zeichensatz))
  random.shuffle(passwort)
  return "".join(passwort)

def passwort_knacken(hashwert, min=6,max=10):
  while True:
    länge = random.randint(min,max)
    passwort = passwort_generieren(länge)
    passwort_hash = hash_berechnen(passwort)
    if passwort_hash == hashwert:
      print(f"Das Passwort lautet {passwort}")
      return passwort
      
if __name__ == "__main__":
  hashwert = "1c0a2e185bd128f8ee0032e2c1d02623bb91b456"
  passwort_knacken(hashwert)