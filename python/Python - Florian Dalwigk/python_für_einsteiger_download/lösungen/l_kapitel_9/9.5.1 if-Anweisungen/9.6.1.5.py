# Der Nutzer wird nach einer Zahl als kleingeschriebenes Wort gefragt.
zahl = input("Gib eine Zahl als kleingeschriebenes Wort ein! ")
# Abhängig von der Eingabe wird die Zahl als Zahl (nicht als Wort) ausgegeben.
if zahl == "eins":
  print(1)
elif zahl == "zwei":
  print(2)
elif zahl == "drei":
  print(3)
elif zahl == "vier":
  print(4)
elif zahl == "fünf":
  print(5)
elif zahl == "sechs":
  print(6)
elif zahl == "sieben":
  print(7)
elif zahl == "acht":
  print(8)
elif zahl == "neun":
  print(9)
elif zahl == "zehn":
  print(10)
# Wenn keine der Zahlen eingegeben wurde, folgt eine gesonderte Ausgabe.
else:
  print("Diese Zahl ist mir nicht bekannt!")