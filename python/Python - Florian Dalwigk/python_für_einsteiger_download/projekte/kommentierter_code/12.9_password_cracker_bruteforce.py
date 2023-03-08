import string as s
import itertools, hashlib

# Zeichensatz für die Passwörter festlegen.
zeichen = s.ascii_letters + s.digits + s.punctuation

# Funktion zum Berechnen des Hashwert eines Textes.
def hash_berechnen(text):
  # SHA1-Hash berechnen.
  sha1_hash = hashlib.sha1(text.encode())
  # Hex-Darstellung des Hashs erzeugen.
  hex_darstellung = sha1_hash.hexdigest()
  # Hex-Darstellung des Hashs zurückgeben.
  return hex_darstellung
  
# Funktion zum Knacken von Passwörtern.
def passwort_knacken(hashwert, min=6,max=10):
  # min- bis max-stellige Passwörter ausprobieren.
  for n in range(min,max+1):
    # Für jede mögliche Buchstabenkombination
    for passwort in itertools.product(zeichen,repeat=n):
      # wird aus dem Tupel ein Passwort-String erzeugt,
      passwort = "".join(passwort)
      # davon der Passwort-Hash berechnet und
      passwort_hash = hash_berechnen(passwort)
      # geprüft, ob der berechnete Passwort-Hash dem vorgegebenen entspricht. Wenn das Passwort gefunden wurde, 
      if passwort_hash == hashwert:
        # wird es ausgegeben
        print(f"Das Passwort lautet {passwort}")
        # und zurückgegeben.
        return passwort
  # Wenn nichts gefunden wurde, wird angezeigt, dass das Passwort mehr als max Stellen hat.
  print(f"Das Passwort hat mehr als {max} Stellen.")

# Hauptprogramm.
if __name__ == "__main__":
  # Hashwert eines Passworts.
  hashwert = "6367c48dd193d56ea7b0baad25b19455e529f5ee" # abc123
  # Passwort mit zufällig generierten Passwörtern knacken.
  passwort_knacken(hashwert)