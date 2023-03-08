"""
In dem Modul "time" gibt es eine Funktion "localtime".
Das Ergebnis des Funktionsaufrufs ist ein Objekt vom Typ <class 'time.struct_time'>.
Relevant sind für uns die folgenden Felder mit den entsprechenden Indizes
0 -> tm_year
1 -> tm_mon
2 -> tm_mday
3 -> tm_hour
4 -> tm_min
5 -> tm_sec
"""
import time
# Zeitstempel auslesen.
z = time.localtime()
# Wir geben den Zeitstempel im gewünschten Format aus.
print(f"{z[2]}.{z[1]}.{z[0]} {z[3]}:{z[4]}:{z[5]}")