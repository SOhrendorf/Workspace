import string as s
import secrets

def passwort_generieren(laenge):
  zeichen = s.ascii_letters + s.digits + s.punctuation
  passwort = ''
  for _ in range(laenge):
    passwort += secrets.choice(zeichen)
  return passwort

if __name__ == "__main__":
  while (n := int(input("Passwortlänge? (mind. 16) "))) < 16:
    pass
  passwort = passwort_generieren(n)
  print(passwort)