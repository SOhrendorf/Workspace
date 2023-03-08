def anzeigen(spielfeld):
  ergebnis = ''
  for spalte in spielfeld:
    for zeile in spalte:
      ergebnis += zeile
    ergebnis += '\n'
  print(ergebnis)
  
def überprüfen(spiel):
  for zeile in spiel:
    if len(set(zeile)) == 1 and '.' not in zeile:
      print(f"Spieler {zeile[0]} gewinnt!")
      quit()
  spalten = [list(e) for e in zip(*spiel)]
  for spalte in spalten:
    if len(set(spalte)) == 1 and '.' not in spalte:
      print(f"Spieler {spalte[0]} gewinnt!")
      quit()
  diag1 = [spiel[i][i] for i in range(3)]
  if len(set(diag1)) == 1 and '.' not in diag1:
    print(f"Spieler {diag1[0]} gewinnt!")
    quit()
  diag2 = [zeile[-i-1] for i,zeile in enumerate(spiel)]
  if len(set(diag2)) == 1 and '.' not in diag2:
    print(f"Spieler {diag2[0]} gewinnt!")
    quit()
  if '.' not in spiel[0] + spiel[1] + spiel[2]:
    print("Unentschieden!")
    quit()

def spielen(spieler, spiel, x, y):
  while spiel[x][y] != '.':
    spielzug = input(f"Feld belegt! Nochmal! ")
    x, y = int(spielzug[0]), int(spielzug[1])
  spiel[x][y] = spieler
  
if __name__ == "__main__":
  spielfeld = [
          ['.','.','.'],
          ['.','.','.'],
          ['.','.','.']
         ]
  anzeigen(spielfeld)
  spieler = 'O'
  
  while True:
    spielzug = input(f"Spieler {spieler}: ")
    x, y = int(spielzug[0]), int(spielzug[1])
    spielen(spieler, spielfeld, x, y)
    anzeigen(spielfeld)
    überprüfen(spielfeld)
    if spieler == 'O':
      spieler = 'X'
    elif spieler == 'X':
      spieler = 'O'