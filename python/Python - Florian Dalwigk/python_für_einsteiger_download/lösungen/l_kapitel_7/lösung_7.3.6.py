import math # Import, um die Wurzelfunktion sqrt nutzen zu können.

# Benutzereingaben abfragen.
a = float(input("Länge der Ankathete: "))
b = float(input("Länge der Gegenkathete: "))

# Länge der Hypotenuse berechnen. Dafür muss man die Wurzel aus dem 
c = math.sqrt(a**2 + b**2) 
# Alternativ kann man auch (a**2 + b**2)**0.5 rechnen. Dann spart man sich den math-Import.

# Ergebnis ausgeben.
print(f"Die Hypotenuse ist {c} cm lang.")