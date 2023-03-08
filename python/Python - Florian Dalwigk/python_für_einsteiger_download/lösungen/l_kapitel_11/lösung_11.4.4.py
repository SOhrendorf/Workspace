"""
In der Variable "sys.version" ist diese Information gespeichert.
Diese Variable speichert allerdings mehr als nur die Versionsnummer.
"""
import sys
# Informationen auslesen.
infos = sys.version
# Nur die Versionsnummer (vor dem ersten Leerzeichen) auslesen.
version = infos.split(" ")[0]
# Version ausgeben.
print(version)