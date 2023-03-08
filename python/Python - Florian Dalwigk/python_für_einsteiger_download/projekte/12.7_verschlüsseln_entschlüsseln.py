import os

def verschlüsseln(dateiname):
  verschlüsseln = open(dateiname, "rb").read()
  größe = len(verschlüsseln)
  schlüssel = os.urandom(größe)
  with open(f"{dateiname}.key", "wb") as datei:
    datei.write(schlüssel)
  verschlüsselt=bytes(a^b for (a,b) in zip(verschlüsseln,schlüssel))
  with open(f"{dateiname}.crypt", "wb") as datei:
    datei.write(verschlüsselt)        

def entschlüsseln(dateiname, schlüssel):
  verschlüsselt = open(dateiname, "rb").read()
  schlüssel = open(schlüssel, "rb").read()
  entschlüsselt=bytes(a^b for (a,b) in zip(verschlüsselt,schlüssel))
  dateiname = "entschlüsselt_" + dateiname[:-6]
  with open(dateiname, "wb") as datei:
    datei.write(entschlüsselt)     

if __name__ == "__main__":
  dateiname = "logo.png"
  verschlüsseln(dateiname)
  entschlüsseln(f"{dateiname}.crypt", f"{dateiname}.key")