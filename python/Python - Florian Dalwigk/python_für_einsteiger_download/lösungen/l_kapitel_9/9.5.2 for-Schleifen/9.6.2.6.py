def matrix_ausgeben(matrix):
  # Es wird eine "leere" String-Variable für das Ergebnis definiert.
  ergebnis = ""
  # Wir gehen nacheinander alle Zeilen durch.
  for i in range(len(matrix)):
    # Wir gehen nacheinander alle Spalten durch.
    for j in range(len(matrix[0])):
      # Das Element in Zeile i und Spalte j wird dem Ergebnis hinzugefügt.
      ergebnis += f"{matrix[i][j]} "
    # Am Ende einer Zeile folgt ein Zeilenumbruch.
    ergebnis += "\n"
  # Das Ergebnis wird ausgegeben. Mit "strip" wird der letzte Zeilenumbruch entfernt.
  print(ergebnis.strip()) 

matrix_ausgeben([[1,2,3,4],[5,6,7,8]])