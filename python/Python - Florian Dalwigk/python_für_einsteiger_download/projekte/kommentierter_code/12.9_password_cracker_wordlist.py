import hashlib
# Funktion zum Berechnen des Hashwert eines Textes.
def hash_berechnen(text):
  # SHA1-Hash berechnen. Hier muss der text nicht mit encode() kodiert werden, weil text bereits in Bytes vorliegt.
  sha1_hash = hashlib.sha1(text)
  # Hex-Darstellung des Hashs erzeugen.
  hex_darstellung = sha1_hash.hexdigest()
  # Hex-Darstellung des Hashs zurückgeben.
  return hex_darstellung
  
# Funktion zum Knacken eines Passworts.
def passwort_knacken(hashwert, wordlist):
  # Wordlist öffnen.
  with open(wordlist, "rb") as datei:
    # Von jedem Passwort in der Wordlist
    for passwort in datei:
      # werden die Leerzeichen am Anfang/Ende entfernt
      passwort = passwort.strip()
      # und der Passwort-Hash berechnet.
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
  hashwert = "88b701448f2ed79371608e359349d416d7ededb9" # lifewithoutprivacy
  # Pfad zur Wordlist definieren.
  wordlist = "rockyou.txt"
  # Passwort mithilfe der Wordlist 'rockyou.txt' knacken.
  passwort_knacken(hashwert, wordlist)
  
# rockyou.txt herunterladen: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt