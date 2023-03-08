from requests import get

def thumbnail_herunterladen(url, dateiname="thumbnail.png"):
  if "youtu.be" in url: 
    id = url.split("/")[3]
  else: 
    id = url.split("=")[1][:11]
  with open(dateiname, "wb") as datei:
    name = "maxresdefault.jpg"
    antwort = get(f"https://img.youtube.com/vi/{id}/{name}")
    datei.write(antwort.content)
    print("Download erfolgreich!")

if __name__ == "__main__":
  url = input("Geben Sie die URL des Videos an: ")
  thumbnail_herunterladen(url)