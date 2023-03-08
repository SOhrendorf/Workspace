passwort_hashes = {
  "s3cr3t" : " a4d80eac9ab26a4a2da04125bc2c096a",
  "n00bsled" : " 1b027a471918e398bad5a8ed98a02bd1",
  "t1m3=money!" : " 36593caf3c79f69112d47e44807ce165"
}

werte = passwort_hashes.values()
werteliste = list(werte)
print(werteliste)
"""
Ausgabe: 
--------------------------------------
['a4d80eac9ab26a4a2da04125bc2c096a', 
'1b027a471918e398bad5a8ed98a02bd1', 
'36593caf3c79f69112d47e44807ce165']
--------------------------------------