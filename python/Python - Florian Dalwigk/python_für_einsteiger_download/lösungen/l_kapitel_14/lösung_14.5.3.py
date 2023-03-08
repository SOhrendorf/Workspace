# Es wird versucht, den BMI zu berechnen.
try: 
  # ValueError: 
  # Hier kann fälschlicherweise etwas eingegeben werden, das keine Zahl ist.
  gewicht = int(input("Gewicht (in kg): "))
  # ValueError: 
  # Hier kann fälschlicherweise etwas eingegeben werden, das keine Zahl ist.
  größe = float(input("Körpergröße (in cm): "))
  # ZeroDivisionError: 
  # Wenn der Benutzer bei "größe" den Wert 0 eingegeben hat, dann erfolgt hier eine Division durch 0.
  bmi = gewicht/größe**2
  print(f"Dein BMI ist {bmi}")
# Hier fangen wir die ValueError Exception ab.
except ValueError:
  print("Es wurde etwas eingegeben, das keine Zahl ist.")
except ZeroDivisionError:
  print("Die Körpergröße wurde mit 0 angegeben, wodurch eine Division durch 0 stattgefunden hat.")