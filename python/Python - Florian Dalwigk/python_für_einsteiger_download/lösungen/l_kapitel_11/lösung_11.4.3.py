"""
Die Funktion "getlogin" des Moduls "os" gibt den Namen des aktuell 
angemeldeten Benutzers aus.
"""
import os
# Nutzername auslesen.
nutzername = os.getlogin()
# Begrüßung.
print(f"Hallo {nutzername}!")