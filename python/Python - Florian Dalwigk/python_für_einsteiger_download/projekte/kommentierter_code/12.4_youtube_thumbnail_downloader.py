from requests import get
# Funktion zum Download eines Thumbnails.
def thumbnail_herunterladen(url, dateiname="thumbnail.png"):
  # Wenn youtu.be in der URL ist (= kurzer Link zum Teilen),
  if "youtu.be" in url: 
    # dann URL am / splitten und das letzte Element (Video-ID) auswählen,
    id = url.split("/")[3]
  else: 
    # ansonsten am = splitten und die 11-stellige Video-ID auslesen.
    id = url.split("=")[1][:11]
  # Thumbnail-Container öffnen, 
  with open(dateiname, "wb") as datei:
    # Name des Thumbnails.
    name = "maxresdefault.jpg"
    # Thumbnail herunterladen und
    antwort = get(f"https://img.youtube.com/vi/{id}/{name}")
    # Thumbnail auf die Festplatte schreiben. 
    datei.write(antwort.content)
    # Mitteilung, dass der Download erfolgreich war, ausgeben.
    print("Download erfolgreich!")

# Hauptprogramm.
if __name__ == "__main__":
  # URL vom Benutzer abfragen.
  url = input("Geben Sie die URL des Videos an: ")
  # Thumbnail herunterladen.
  thumbnail_herunterladen(url)