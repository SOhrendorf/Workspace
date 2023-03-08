infos = {
  "Florian" : 25,
  "Ayumi" : 28,
  "Eva" : 51,
  "Herbert" : 60
}

# Zuerst werden die Schlüssel mit der Funktion keys() ausgelesen und einer Variable "namen" zugewiesen.
namen = infos.keys()
# Mit der Funktion list() wandeln wir das Ergebnis in eine Liste um.
namensliste = list(namen)

# Zuerst werden die Werte mit der Funktion values() ausgelesen und einer Variable "werte" zugewiesen.
werte = infos.values()
# Mit der Funktion list() wandeln wir das Ergebnis in eine Liste um.
altersliste = list(werte)

# Wir können uns anschauen, wie die Ergebnisse aussehen (optional).
print(namensliste)
print(altersliste)