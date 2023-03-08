# Der Nutzer wird nach einer Zahl als kleingeschriebenes Wort gefragt.
zahl = input("Gib eine Zahl als kleingeschriebenes Wort ein! ")
# Abhängig von der Eingabe wird die Zahl als Zahl (nicht als Wort) ausgegeben.
match zahl:
  case "eins":
    print(1)
  case "zwei":
    print(2)
  case "drei":
    print(3)
  case "vier":
    print(4)
  case "fünf":
    print(5)
  case "sechs":
    print(6)
  case "sieben":
    print(7)
  case "acht":
    print(8)
  case "neun":
    print(9)
  case "zehn":
    print(10)
  case "eins":
    print(1)
  # Wenn keine der Zahlen eingegeben wurde, folgt eine gesonderte Ausgabe.
  case _:
    print("Diese Zahl ist mir nicht bekannt!")