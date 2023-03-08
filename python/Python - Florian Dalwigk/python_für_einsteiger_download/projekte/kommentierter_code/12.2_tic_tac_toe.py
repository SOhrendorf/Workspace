# Funktion zur Anzeige des Spielfelds mit den aktuellen Zügen. 
def anzeigen(spielfeld):
  # Ergebnisvariable, die später angezeigt werden soll.
  ergebnis = ''
  # Alle Zeilen und Spalten durchlaufen ...
  for spalte in spielfeld:
    for zeile in spalte:
      # Das aktuelle Element wird der Ergebnisvariable hinzugefügt. 
      ergebnis += zeile
    # Zeilenumbruch.
    ergebnis += '\n'
  # Ergebnis anzeigen.
  print(ergebnis)

# Diese Funktion überprüft, ob das Spiel vorbei ist oder alle Felder befüllt sind.
def überprüfen(spiel):
  # Zeilen checken.
  for zeile in spiel:
    if len(set(zeile)) == 1 and '.' not in zeile:
      print(f"Spieler {zeile[0]} gewinnt!")
      quit()
  # Spalten checken.
  spalten = [list(e) for e in zip(*spiel)]
  for spalte in spalten:
    if len(set(spalte)) == 1 and '.' not in spalte:
      print(f"Spieler {spalte[0]} gewinnt!")
      quit()
  # Hier wird die Hauptdiagonale (oben links nach unten rechts) erstellt.
  diag1 = [spiel[i][i] for i in range(3)]
  # Hauptdiagonale checken.
  if len(set(diag1)) == 1 and '.' not in diag1:
    print(f"Spieler {diag1[0]} gewinnt!")
    quit()
  # Hier wird die Nebendiagonale (unten links nach oben rechts) erstellt.
  diag2 = [zeile[-i-1] for i,zeile in enumerate(spiel)]
  # Nebendiagonale checken.
  if len(set(diag2)) == 1 and '.' not in diag2:
    print(f"Spieler {diag2[0]} gewinnt!")
    quit()
  # Alles befüllt?
  if '.' not in spiel[0] + spiel[1] + spiel[2]:
    print("Unentschieden!")
    quit()

# Mit dieser Funktion kann ein Spieler einen Spielszug unternehmen.
def spielen(spieler, spiel, x, y):
  # Solange der Spieler seinen Stein auf ein besetztes Feld zu setzen versucht, 
  while spiel[x][y] != '.':
    # wird die Eingabe des Benutzers ausgelesen. Es wird bei 0 zu zählen begonnen. Zuerst wird die Zeile und dann die Spalte adressiert.
    # Die Eingabe 21 bedeutet z. B. "3. Zeile, 2. Spalte".
    spielzug = input(f"Feld belegt! Nochmal! ")
    x, y = int(spielzug[0]), int(spielzug[1])
  # Der Spielstein des Spielers wird platziert.
  spiel[x][y] = spieler

# Hauptprogramm.
if __name__ == "__main__":
  # Das ist das Spielfeld, auf dem Tic Tac Toe gespielt wird. '.' ist ein leeres Feld.
  spielfeld = [
          ['.','.','.'],
          ['.','.','.'],
          ['.','.','.']
         ]
  # Das Spielfeld wird erstmalig angezeigt.
  anzeigen(spielfeld)
  # Es gibt die Spieler 'O' und 'X'. Es wird mit dem Spieler O begonnen.
  spieler = 'O'
  # In einer Endlosschleife spielen nacheinander die Spieler 'O' und 'X' gegeneinander.
  while True:
    # Der Spieler gibt ein, auf welche Koordinate er seinen Stein setzen will.
    spielzug = input(f"Spieler {spieler}: ")
    # Die eingegebenen Koordinaten werden ausgelesen.
    x, y = int(spielzug[0]), int(spielzug[1])
    # Der Spieler macht seinen Zug.
    spielen(spieler, spielfeld, x, y)
    # Das Spielfeld wird angezeigt.
    anzeigen(spielfeld)
    # Das Spielfeld wird überprüft. Hat schon jemmand gewonnnen? Geht das Spiel unentschieden aus?
    überprüfen(spielfeld)
    # Nach jedem Zug werden die Spieler getauscht.
    if spieler == 'O':
      spieler = 'X'
    elif spieler == 'X':
      spieler = 'O'