namen = ["Anna","Bella","Charlotte","Diana","Erika","Fiona"]
"""
Um die Namen samt ihren Indizes auszugeben, verwenden wir die Methode enumerate.
Die Indizes und Werte speichern wir in jeweils einer Variable.
"""
for i, name in enumerate(namen):
  print(f"{i} : {name}")