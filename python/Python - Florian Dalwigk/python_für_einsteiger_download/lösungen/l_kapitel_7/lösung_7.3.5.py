# Benutzereingaben abfragen.
btc = float(input("Wie viele BTC hast du? "))

# Den Faktor findet man über die Google-Suche https://www.google.de/search?q=bitcoin+in+euro+factor
# Wert am 16.06.2022: 20855.140101
faktor = float(input("Wie hoch ist der Umrechnungsfaktor? "))

# BTC in Euro umrechnen.
euro = btc * faktor

# Ergebnis ausgeben.
print(f"{btc} BTC = {euro} €")