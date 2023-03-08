import fitness                          # 1. Modul "gewicht" Importieren

bmi = fitness.bmi(82,1.87)              # 2. BMI berechnen und einer Variable zuweisen.
bmi = round(bmi,2)                      # 2. BMI auf zwei Nachkommastellen runden. 
print(f"BMI: {bmi}")                    # 2. BMI ausgeben.

gewicht = fitness.abnehmen(77,10)       # 3. Gewicht berechnen.
print(f"Gewicht (Abnahme): {gewicht}")  # 3. Gewicht ausgeben.

gewicht = fitness.zunehmen(56,5)        # 4. Gewicht berechnen.
print(f"Gewicht (Zunahme): {gewicht}")  # 4. Gewicht ausgeben.

name = "Timo"                           # 5. Name "Timo" in einer Variable speichern.
fitness.sag_hallo(name)                 # 5. "Timo" grüßen.