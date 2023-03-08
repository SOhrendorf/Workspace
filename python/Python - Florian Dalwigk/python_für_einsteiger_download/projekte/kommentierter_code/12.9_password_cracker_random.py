import string as s
import hashlib, random

# Funktion zum Berechnen des Hashwert eines Textes.
def hash_berechnen(text):
  # SHA1-Hash berechnen.
  sha1_hash = hashlib.sha1(text.encode())
  # Hex-Darstellung des Hashs erzeugen.
  hex_darstellung = sha1_hash.hexdigest()
  # Hex-Darstellung des Hashs zurückgeben.
  return hex_darstellung

# Funktion zum Generieren von Passwörtern.
def passwort_generieren(laenge):
  # Zeichensatz 
  gross = s.ascii_uppercase
  klein = s.ascii_lowercase
  zahlen = s.digits
  sonderzeichen = s.punctuation
  zeichen = [gross,klein,zahlen,sonderzeichen]
  # Liste mit Zeichen für das finale Passwort.
  passwort = [] 
  # Von jedem der 4 Zeichentypen wird je eines zufällig gewählt.
  for x in zeichen:
    passwort.append(random.choice(x))
  # Die 4 Zeichentypen werden in EINEN String umgewandelt.
  zeichensatz = "".join(zeichen)
  # Solange die Länge des Passworts kleiner als die vorgegebene Länge ist,
  while len(passwort) < laenge:
    # wird aus dem Zeichensatz ein zufälliges Passwort gewählt und der Passwortzeichenliste hinzugefügt.
    passwort.append(random.choice(zeichensatz))
  # Die Passwortzeichenliste wird noch einmal durchgemischt. Sonst ist der 1. Buchstabe groß, der 2. klein, der 3. eine Zahl und der 4. ein Sonderzeichen (vorhersehbar).
  random.shuffle(passwort)
  # Die Liste mit den Passwortzeichen wird zu einem String zusammengesetzt und zurückgegeben.
  return "".join(passwort)

# Funktion zum Knacken von Passwörtern.
def passwort_knacken(hashwert, min=6,max=10):
  while True:
    # Länge der Passwortkandidaten festlegen.
    länge = random.randint(min,max)
    # Zufälliges Passwort generieren.
    passwort = passwort_generieren(länge)
    # Hashwert des zufällig generierten Passworts berechnen.
    passwort_hash = hash_berechnen(passwort)
    # Wenn der berechnete Passwort-Hash dem vorgegebenen entspricht, 
    if passwort_hash == hashwert:
      # wird das Passwort ausgegeben
      print(f"Das Passwort lautet {passwort}")
      # und zurückgegeben.
      return passwort
      
# Hauptprogramm.  
if __name__ == "__main__":
  # Hashwert eines Passworts.
  hashwert = "1c0a2e185bd128f8ee0032e2c1d02623bb91b456"
  # Passwort mit zufällig generierten Passwörtern knacken.
  passwort_knacken(hashwert)