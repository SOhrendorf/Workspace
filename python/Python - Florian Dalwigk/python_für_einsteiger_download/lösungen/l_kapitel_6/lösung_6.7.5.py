# Wir importieren alle Funktionen außer "sag_hallo".
from fitness import bmi, abnehmen, zunehmen

# Beispiele
bmi = bmi(82,1.87)
bmi = round(bmi,2)
print(f"BMI: {bmi}")

gewicht = abnehmen(77,10)
print(f"Gewicht (Abnahme): {gewicht}")

gewicht = zunehmen(56,5)
print(f"Gewicht (Zunahme): {gewicht}")
