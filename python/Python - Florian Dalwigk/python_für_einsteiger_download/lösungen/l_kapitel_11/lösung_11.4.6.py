"""
Im Modul "random" gibt es dafür die Funktion "sample". 
Diese erhält zwei Parameter. 
Der erste Parameter ist eine Liste mit den Elementen, aus denen ausgewählt wird.
Der zweite Parameter gibt an, wie viele Elemente zufällig ausgewählt werden sollen.
"""
import random
# Liste mit Zahlen, aus denen ausgewählt werden soll, erzeugen.
zahlen = range(1,101)
# Zahlen auswählen und ausgeben.
print(random.sample(zahlen,5))