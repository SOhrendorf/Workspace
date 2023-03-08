import hashlib

def hash_berechnen(text):
  sha1_hash = hashlib.sha1(text)
  hex_darstellung = sha1_hash.hexdigest()
  return hex_darstellung
  
def passwort_knacken(hashwert, wordlist):
  with open(wordlist, "rb") as datei:
    for passwort in datei:
      passwort = passwort.strip()
      passwort_hash = hash_berechnen(passwort)
      if passwort_hash == hashwert:
        print(f"Das Passwort lautet {passwort}")
        return passwort
        
if __name__ == "__main__":
  hashwert = "88b701448f2ed79371608e359349d416d7ededb9" 
  wordlist = "rockyou.txt"
  passwort_knacken(hashwert, wordlist)