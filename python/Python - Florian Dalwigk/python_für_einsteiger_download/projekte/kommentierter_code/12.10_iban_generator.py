from requests import get
import random
# Datei aus dem Internet herunterladen
def datei_herunterladen(url, dateiname="blz.txt"):
  # Container für die Datei aus dem Internet vorbereiten.
  with open(dateiname, "wb") as datei:
    # Antwort von der Datei hinter der URL speichern.
    antwort = get(url)
    # Antwort auf die Festplatte schreiben.
    datei.write(antwort.content)

# Funktion zum Generieren von IBAN-Nummern.
def iban_generieren(bankleitzahlen):
  # Ländercode.
  DE = "131400"
  # Aus der Liste aller Bankleitzahlen wird eine zufällig ausgewählt.
  blz = random.choice(bankleitzahlen)
  # Zufällige Kontonummer generieren.
  kontonummer = str(random.randint(100000, 9999999999)).zfill(10)
  # Prüfziffer berechnen.
  prüfziffer = str(98 - int(blz + kontonummer + DE)%97).zfill(2)
  # IBAN zusammensetzen.
  IBAN = "DE" + prüfziffer + blz + kontonummer
  # IBAN ausgeben.
  print(IBAN)
  # IBAN zurückgeben.
  return IBAN

# Hauptprogramm.
if __name__ == "__main__":
  # Bankleitzahlen-Datei von der Bundesbank herunterladen.
  datei_herunterladen("https://www.bundesbank.de/resource/blob/602632/d025696e366a91063fb307cc1f73e0d5/mL/blz-aktuell-txt-data.txt")
  # Set zum Speichern von Bankleitzahlen. Ein Set wird verwendet, um Duplikate aus der heruntergeladenen Datei zu entfernen.
  bankleitzahlen = set()
  # Bankleitzahlen-Datei herunterladen.
  with open("blz.txt", "r") as datei:
    # Zeilen auslesen und abspeichern.
    zeilen = datei.read().splitlines()
    # Duplikate entfernen und als Liste abspeichern.
  for zeile in zeilen:
    bankleitzahlen.add(zeile[:8])
  # Bankleitzahlen-Set in eine Liste umwandeln.
  bankleitzahlen = list(bankleitzahlen)
  # IBAN generieren.
  iban_generieren(bankleitzahlen)