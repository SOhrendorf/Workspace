zahlen = [0,1,2,3,4,5] 

zahlen[2] = 5                       
# Ergebnis: [0, 1, 5, 3, 4, 5]
# Die 2 wird durch eine 5 ersetzt.

zahlen.remove(1)
# Ergebnis: [0, 5, 3, 4, 5]
# Die 1 wird entfernt.

zahlen.append(7)
# Ergebnis: [0, 5, 3, 4, 5, 7]
# Die 7 wird ganz hinten angehängt.

zahlen.remove(4)
# Ergebnis: [0, 5, 3, 5, 7]
# Die 4 wird entfernt.

zahlen += [1,2,3]
# Ergebnis: [0, 5, 3, 5, 7, 1, 2, 3]
# Es wird die Liste [1,2,3] ganz hinten angehängt.

zahlen.insert(3,0)
# Ergebnis: [0, 5, 3, 0, 5, 7, 1, 2, 3]
# An dem Index 3 (das ist die 5) wird eine 0 eingefügt und der Rest jeweils um eine Position nach rechts geschoben.

zahlen.sort(reverse=True)
# Ergebnis: [7, 5, 5, 3, 3, 2, 1, 0, 0]
# Die Liste wird (beginnend bei der höchsten Zahl) sortiert. 

zahlen.insert(2,3)
# Ergebnis: [7, 5, 3, 5, 3, 3, 2, 1, 0, 0]
# An dem Index 2 (das ist die 5) wird eine 3 eingefügt und der Rest jeweils um eine Position nach rechts geschoben.

zahlen.append(zahlen.count(0))
# Ergebnis: [7, 5, 3, 5, 3, 3, 2, 1, 0, 0, 2]
# zahlen.count(0) ergibt 2, weil es zwei Nullen in der Liste gibt.
# Diese zwei wird durch die Methode append ganz hinten in die Liste eingefügt.

zahlen.remove(zahlen.index(3))
# Ergebnis: [7, 5, 3, 5, 3, 3, 1, 0, 0, 2]
# zahlen.index(3) ergibt 2, weil sich die erste auftretende 3 an der Position 2 befindet.
# Jetzt wird durch die Methode remove die erste auftretende 2 gelöscht.

zahlen.clear()
# Ergebnis: []
# Der Inhalt der Liste wird vollständig gelöscht.