def iban_prüfen(IBAN):
  ländercode = IBAN[:2]
  pruefziffer = IBAN[2:4]
  blz = IBAN[4:12]
  kontonummer = IBAN[12:].zfill(10)
  DE = "131400"
  check = str(98 - int(blz + kontonummer + DE)%97).zfill(2)
  if check == pruefziffer:
    print("Die eingegebene IBAN ist korrekt!")
  else:
    print("Die eingegebene IBAN ist falsch!")

if __name__ == "__main__":
  IBAN = input("Geben Sie bitte Ihre IBAN ein: ")
  iban_prüfen(IBAN)