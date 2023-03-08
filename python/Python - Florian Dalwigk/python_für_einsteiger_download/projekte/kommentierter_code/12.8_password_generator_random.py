import random
import string as s
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

# Hauptprogramm.
if __name__ == "__main__":
  # Die gewünschte Passwortlänge wird vom Benutzer abgefragt.
  n = int(input("Passwortlänge? "))
  # Mithilfe der Funktion "passwort_generieren" wird ein Passwort generiert.
  passwort = passwort_generieren(n)
  # Das Passwort wird ausgegeben.
  print(passwort)

# BSI-Empfehlungen:
# https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Accountschutz/Sichere-Passwoerter-erstellen/sichere-passwoerter-erstellen_node.html
# https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile