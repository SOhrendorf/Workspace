# Gewicht in kg, groesse in m.
def bmi(gewicht,groesse):
  BMI = gewicht/groesse**2
  return BMI
  
# Gewicht in kg, abnahme in kg
def abnehmen(gewicht,abnahme):
  return gewicht-abnahme

# Gewicht in kg, zunahme in kg
def zunehmen(gewicht,zunahme):
  return gewicht+zunahme

def sag_hallo(name):
  print(f"Hallo {name}!")