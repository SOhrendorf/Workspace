import string as s
import itertools, hashlib

zeichen = s.ascii_letters + s.digits + s.punctuation

def hash_berechnen(text):
  sha1_hash = hashlib.sha1(text.encode())
  hex_darstellung = sha1_hash.hexdigest()
  return hex_darstellung
  
def passwort_knacken(hashwert, min=6,max=10):
  for n in range(min,max+1):
    for passwort in itertools.product(zeichen,repeat=n):
      passwort = ''.join(passwort)
      passwort_hash = hash_berechnen(passwort)
      if passwort_hash == hashwert:
        print(f"Das Passwort lautet {passwort}")
        return passwort
  print(f"Das Passwort hat mehr als {max} Stellen.")

if __name__ == "__main__":
  hashwert = "6367c48dd193d56ea7b0baad25b19455e529f5ee"
  passwort_knacken(hashwert)