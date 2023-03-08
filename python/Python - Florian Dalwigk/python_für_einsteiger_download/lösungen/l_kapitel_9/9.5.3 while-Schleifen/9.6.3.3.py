matrix = [[1,0,0],[0,1,0],[0,0,1]]
zeilen = len(matrix)
spalten = len(matrix[0])
i = 0
j = 0 
ergebnis = ""
while i < zeilen:
  while j < spalten:
    ergebnis += str(matrix[i][j])
    j += 1
  ergebnis += "\n"
  j = 0
  i += 1
print(ergebnis)

# Als for-Schleife:
ergebnis = ""
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    ergebnis += str(matrix[i][j])
  ergebnis += "\n"
print(ergebnis.strip())