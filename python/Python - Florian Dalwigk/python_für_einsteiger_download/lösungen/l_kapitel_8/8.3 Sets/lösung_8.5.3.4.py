def prüfen(zahl,zahlen):
  return zahl in zahlen 
  # Wir suchen hier die "zahl" in dem Set "zahlen".
  # Wenn sie gefunden wird, dann ist der Ausdruck "zahl in zahlen" True, sonst False.
  # Das Ergebnis wird dann zurückgegeben.
  
# Beispiel: 
zahlen = {0,1,2,3,4,5}
print(prüfen(1,zahlen)) # True, weil 1 in dem Set "zahlen" enthalten ist.
print(prüfen(7,zahlen)) # False, weil 7 nicht in dem Set "zahlen" enthalten ist.
