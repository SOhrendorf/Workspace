buchstaben = ['A','B','C','D','E','F','G','H','I','J','K','L'] 

buchstaben[2:5]      
# Ergebnis: ['C', 'D', 'E']
           
buchstaben[-5:-1]
# Ergebnis: ['H', 'I', 'J', 'K']
# Wir starten beim Index -5 ('H') und gehen bis ein Element vor dem 'L' (Index -1).

buchstaben[:]
# Ergebnis: ['A','B','C','D','E','F','G','H','I','J','K','L']  
# Da der Start- und Endindex nicht angegeben werden, wird die gesamte Liste betrachtet.

buchstaben[5:]
# Ergebnis: ['F', 'G', 'H', 'I', 'J', 'K', 'L']
# Der Startindex ist 5 ('F'). 
# Der der Endindex angegeben wird, wird der Rest der Liste ab dem Startindex betrachtet.

buchstaben[:3]
# Ergebnis: ['A', 'B', 'C']
# Da der Startindex nicht angegeben wird, starten wir direkt am Anfang ('A').
# Der Endindex ist 3, d.h. wir betrachten alles bis ein Element vor dem 'D' (Index 3).

buchstaben[:-5]
# Ergebnis: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Da der Startindex nicht angegeben wird, starten wir direkt am Anfang ('A').
# Der Endindex ist -5. Das ist das Element 'H'. Wir laufen bis ein Element vor dem 'H'.

buchstaben[2:2]
# Ergebnis: []
# Da Start- und Endindex gleich sind, bleibt die Liste leer.

buchstaben[::2]
# Ergebnis: ['A', 'C', 'E', 'G', 'I', 'K']
# Da der Start- und Endindex nicht angegeben werden, wird die gesamte Liste betrachtet.
# Die Zahl 2 hinter dem zweiten Doppelpunkt gibt die Schrittweite 2 an, d.h. es wird jeder zweite Buchstabe in die Liste gepackt.

buchstaben[2::2]
# Ergebnis: ['C', 'E', 'G', 'I', 'K']
# Der Startindex ist 2, d.h. die Liste beginnt ab dem 'C'.
# Da der Endindex nicht angegeben werden, wird alles ab dem 'C' betrachtet.
# Die Zahl 2 hinter dem zweiten Doppelpunkt gibt die Schrittweite 2 an, d.h. es wird jeder zweite Buchstabe ab dem 'C' in die Liste gepackt.

buchstaben[-50:50]
# Ergebnis ['A','B','C','D','E','F','G','H','I','J','K','L'] 
# Es wird die gesamte Liste ausgegeben, weil der Start- bzw. Endindex außerhalb von 0 bzw. 12 liegen.

buchstaben[:len(buchstaben)] 
# Ergebnis: ['A','B','C','D','E','F','G','H','I','J','K','L']  
# Der Startindex ist 0. Dieser wurde allerdings weggelassen.
# len(buchstaben) = 12, weil die Liste 12 Elemente enthält. 
# Der Endindex ist 12, d.h. die Liste läuft von 0 bis (einschließlich) zum letzten Element. 