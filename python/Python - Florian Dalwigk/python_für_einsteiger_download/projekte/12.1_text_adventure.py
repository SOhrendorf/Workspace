import random

ja_nein = ["ja", "nein"]
richtungen = ["links", "rechts", "vorne", "hinten"]
name = input("Wie lautet dein Name, tapferer Recke? ")
print(f"Sei gegrüßt, {name}. Lass uns starten!")
print("Du befindest dich am Rande eines dunklen Waldes.")
print("Kannst du ihn durchqueren?\n")
antwort = ""

while antwort not in ja_nein:
  antwort = input("Möchtest du den Wald betreten? ")
  if antwort == "ja":
    print("Du gehst in den Wald.\n")
  elif antwort == "nein":
    print(f"Du bist wohl noch nicht bereit, {name}! Bis bald!")
    quit()
  else: 
    print("Sorry, das habe ich nicht verstanden.\n")
antwort = ""

while antwort not in richtungen:
  print("Links befindet sich ein Wolf.")
  print("Rechts geht es tiefer in den Wald hinein.")
  print("Direkt vor der befindet sich eine Felswand.")
  print("Hinter dir ist der Ausgang des Waldes.\n")
  antwort = input("In welche Richtung gehst du? ")
  if antwort == "links":
    while antwort not in ja_nein:
      antwort = input("Vor dir steht ein Wolf! Kämpfen? ")
      if antwort == "ja":
        chance = random.uniform(0,1)
        if chance <= 0.6:
          print(f"Der Wolf frisst dich. Lebe wohl, {name}!")
          quit()
        else:
          print(f"Du besiegst den Wolf und findest das Ziel.")
          quit()
      elif antwort == "nein":
        print("Du fliehst erfolgreich vor einem Kampf.")
  elif antwort == "rechts":
    print("Du gehst tiefer in den Wald und verläufst dich.\n")
    quit()
  elif antwort == "vorne":
    while antwort not in ja_nein:
      antwort = input("Möchtest du die Wand erklimmen? ")
      if antwort == "ja":
        chance = random.uniform(0,1)
        if chance <= 0.4:
           print("Du rutschst ab, fällst und stirbst.")
           quit()
        else: 
          print("\nOben angekommen siehst du den Waldausgang.") 
      else:
        print(f"Ok, {name}.")
  elif antwort == "hinten":
    print(f"Du verlässt den Wald. Tschau,{name}!")
    quit()
  else:
    print("Sorry, das habe ich nicht verstanden.\n")