# Funktion zum Überprüfen einer IBAN-Nummer.
def iban_prüfen(IBAN):
  # Ländercode auslesen. Wird hier nicht benötigt, da wir von Deutschen IBAN-Nummern ausgehen.
  ländercode = IBAN[:2]
  # Prüfziffer auslesen.
  pruefziffer = IBAN[2:4]
  # Bankleitzahl auslesen.
  blz = IBAN[4:12]
  # Kontonummer auf 10 Stellen auffüllen, falls nötig.
  kontonummer = IBAN[12:].zfill(10)
  # Ländercode für Deutschland definieren.
  DE = "131400"
  # Prüfziffer aus den ausgelesenen Daten berechnen.
  check = str(98 - int(blz + kontonummer + DE)%97).zfill(2)
  # Prüfen, ob die ausgelesene Prüfziffer der von uns berechneten entspricht.
  if check == pruefziffer:
    print("Die eingegebene IBAN ist korrekt!")
  else:
    print("Die eingegebene IBAN ist falsch!")

# Hauptprogramm.
if __name__ == "__main__":
  # IBAN eingeben.
  IBAN = input("Geben Sie bitte Ihre IBAN ein: ")
  # IBAN überprüfen.
  iban_prüfen(IBAN)