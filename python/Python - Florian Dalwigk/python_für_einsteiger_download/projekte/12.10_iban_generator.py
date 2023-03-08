from requests import get
import random

def datei_herunterladen(url, dateiname="blz.txt"):
  with open(dateiname, "wb") as datei:
    antwort = get(url)
    datei.write(antwort.content)

def iban_generieren(bankleitzahlen):
  DE = "131400"
  blz = random.choice(bankleitzahlen)
  kontonummer = str(random.randint(100000, 9999999999)).zfill(10)
  prüfziffer = str(98 - int(blz + kontonummer + DE)%97).zfill(2)
  IBAN = "DE" + prüfziffer + blz + kontonummer
  print(IBAN)
  return IBAN

if __name__ == "__main__":
  datei_herunterladen("https://www.bundesbank.de/resource/blob/602632/d025696e366a91063fb307cc1f73e0d5/mL/blz-aktuell-txt-data.txt")
  bankleitzahlen = set()
  with open("blz.txt", 'r') as datei:
    zeilen = datei.read().splitlines()
  for zeile in zeilen:
    bankleitzahlen.add(zeile[:8])
  bankleitzahlen = list(bankleitzahlen)
  iban_generieren(bankleitzahlen)