name = "Tux"
i = 42                                      
liste = [i, name, True]                                         
j = 42                                                          
wörterbuch = {"Tuxedo" : "anzug", "Mask" : "Maske"}

# Keine Exception, weil i ein Integer ist.   
int(i)     

# ValueError Exception, weil in "Tux" kein Float steckt.                                                     
float(name)

# IndexError Exception, weil der Index 3 eine Liste mit mindestens 4 Elementen voraussetzt.
liste[3]

# ZeroDivisionError Exception, weil i-j=42-42=0 ist und so durch 0 geteilt wird.
i/(i-j)

# Keine Exception, weil liste[i-40]=liste[42-40]=liste[2]=True ist.
liste[i-40]

# SyntaxError Exception, weil der String mit einem ' begonnen und mit einem " beendet wird.
print(f'Hallo {name}!")

# KeyError Exception, weil der Schlüsel "Maske" nicht in dem Dictionary zu finden ist.
wörterbuch["Maske"]

# IndentationError Exception, weil die Anweisung ohne Grund eingerückt ist.
  bool(name)
  
# Keine Exception, weil nach dem Schlüssel "Tuxedo" in dem Dictionary gesucht wird und dieser existiert.
wörterbuch[name + "edo"]

# ZeroDivisionError Exception, weil j%6=42%6=0 ist.
i/(j%6)

# FileNotFoundError Exception, weil die Datei "test.txt" nicht existiert.
datei = open("test.txt",'r') # "test.txt" existiert nicht.