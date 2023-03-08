# Wir verwenden **kwargs, denen wir die Default-Werte aus der Aufgabenstellung zuweisen.
def sag_hallo(**daten):
  vorname = daten.get("vorname","Marla")
  nachname = daten.get("nachname","Musterfrau")
  strasse = daten.get("strasse","Musterstraße")
  hausnummer = daten.get("hausnummer",42)
  plz = daten.get("plz",31337)
  ort = daten.get("ort","Leethausen")
  # Ausgabe.
  print(f"{vorname} {nachname}\n{strasse} {hausnummer}\n{plz} {ort}")

sag_hallo()