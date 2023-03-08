a = 2.5
b = -5
c = 20
d = "Hallo"
e = "Python"

d + " " + e         # Lösung: Hallo Python
c % 7               # Lösung: 6
16**(a - 2)         # Lösung: 4.0
d**c                # Lösung: FEHLER!!! Man kann keinen String potenzieren.
(b + c) / b         # Lösung: -3.0
20**(2 * a + b)     # Lösung: 1.0. Hier steht nicht 1, weil 20**0.0 und nicht 20**0 gerechnet wird.
2 * a * d           # Lösung: FEHLER!!! Als Zwischenergebnis kommt 5.0 heraus. Die Multiplikation von String funktioniert nicht mit Floats.
(c - b) // 7        # Lösung: 3
e // "Python"       # Lösung: FEHLER!!! Man kann nicht durch einen String dividieren.
b**2 - 25           # Lösung: 0
