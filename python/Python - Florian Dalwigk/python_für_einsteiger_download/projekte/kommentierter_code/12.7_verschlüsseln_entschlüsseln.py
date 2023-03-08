import os
# Funktion zum Verschlüsseln von Dateien.
def verschlüsseln(dateiname):
  # Datei, die verschlüsselt werden soll.
  verschlüsseln = open(dateiname, "rb").read()
  # Größe der zu verschlüsselnden Datei.
  größe = len(verschlüsseln)
  # Schlüsselgenerierung. Dieser ist so lang wie die Datei selbst.
  schlüssel = os.urandom(größe)
  # Schlüssel speichern.
  with open(f"{dateiname}.key", "wb") as datei:
    datei.write(schlüssel)
  # Datei mit dem One-Time-Pad verschlüsseln.
  verschlüsselt=bytes(a^b for (a,b) in zip(verschlüsseln,schlüssel))
  # Verschlüsselte Datei auf die Festplatte schreiben.
  with open(f"{dateiname}.crypt", "wb") as datei:
    datei.write(verschlüsselt)        

# Funktion zum Entschlüsseln von verschlüsselten Dateien.
def entschlüsseln(dateiname, schlüssel):
  # Verschlüsselte Datei einlesen.
  verschlüsselt = open(dateiname, "rb").read()
  # Schlüssel einlesen.
  schlüssel = open(schlüssel, "rb").read()
  # Datei mit dem One-Time-Pad entschlüsseln.
  entschlüsselt=bytes(a^b for (a,b) in zip(verschlüsselt,schlüssel))
  # .crypt aus dem Dateinamen entfernen.
  dateiname = "entschlüsselt_" + dateiname[:-6]
  # Entschlüsselte Datei auf die Festplatte schreiben.
  with open(dateiname, "wb") as datei:
    datei.write(entschlüsselt)     

# Hauptprogramm.
if __name__ == "__main__":
  # Name bzw. Pfad zur Datei, die verschlüsselt werden soll.
  dateiname = "logo.png"
  # Datei verschlüsseln.
  verschlüsseln(dateiname)
  # Name der Datei, die entschlüsselt werden soll.
  entschlüsseln(f"{dateiname}.crypt", f"{dateiname}.key")