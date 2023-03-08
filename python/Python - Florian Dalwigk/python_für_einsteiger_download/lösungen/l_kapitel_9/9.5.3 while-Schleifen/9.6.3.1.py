"""
Keine Endlosschleife.
'True and False' ergibt den Wert 'False'.
Die Schleife wird also nie betreten.
"""
while True and False:
  print("Ich bin ein Text.")
  
"""
Keine Endlosschleife.
Die Schleife wird nie betreten, 
weil 'weitermachen' den Wert 'False' hat.
"""
weitermachen = False
while weitermachen:
  weitermachen = True
  if weitermachen:
    print("Das Programm wird ausgeführt.")
  else:
    print("Das Programm wird nicht ausgeführt.")

"""
Endlosschleife.
Die Variable 'zahl' hat am Anfang den Wert 3. 
'zahl % 2' ist somit nicht 0.
Da 'zahl' immer nur mit 3 multipliziert wird, 
wird das Ergebnis von zahl % 2 nie 0.
"""
zahl = 3
while zahl % 2 != 0:
  print(zahl)
  zahl = zahl * 3

"""
Endlosschleife. 
Egal, was der Benutzer eingibt: 
Der Wert 'weitermachen' wird stets auf True gesetzt.
Wenn 'False' eingegeben wird, dann bleibt 'weitermachen' auf 'True'.
"""
weitermachen = True
while weitermachen:
  weitermachen = input("Weitermachen? ")
  if weitermachen != False:
    weitermachen = True
