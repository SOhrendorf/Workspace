# Benutzereingaben abfragen.
gewicht = float(input("Wie schwer bist du? (kg) "))
groesse  = float(input("Wie groß bist du? (m) "))

# BMI berechnen.
bmi = gewicht/groesse**2

# Ergebnis ausgeben.
print(f"Dein BMI ist {bmi}.")