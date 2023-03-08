import string as s
import secrets

# Funktion zum Generieren von Passwörtern.
def passwort_generieren(laenge):
  # Zeichensatz 
  zeichen = s.ascii_letters + s.digits + s.punctuation
  # Liste mit Zeichen für das finale Passwort.
  passwort = "" 
  # Von jedem der 4 Zeichentypen wird je eines zufällig gewählt.
  while len(passwort) < laenge:
    # wird aus dem Zeichensatz ein zufälliges Passwort gewählt und dem Passwort hinzugefügt.
    passwort += secrets.choice(zeichen)
  # Die Liste mit den Passwortzeichen wird zu einem String zusammengesetzt und zurückgegeben.
  return passwort

# Hauptprogramm.
if __name__ == "__main__":
  # Die gewünschte Passwortlänge wird vom Benutzer abgefragt.
  while (n := int(input("Passwortlänge? (mind. 16) "))) < 16:
    pass
  # Mithilfe der Funktion "passwort_generieren" wird ein Passwort generiert.
  passwort = passwort_generieren(n)
    # Das Passwort wird ausgegeben.
  print(passwort)

# BSI-Empfehlungen:
# https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Accountschutz/Sichere-Passwoerter-erstellen/sichere-passwoerter-erstellen_node.html
# https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile