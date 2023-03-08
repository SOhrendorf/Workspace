zahlen = {
  "eins" : 1,
  "zwei" : 2,
  "drei" : 3
}
del zahlen["zwei"]
print(zahlen)
# Ausgabe: {'eins': 1, 'drei': 3}
del zahlen["vier"] # KeyError: 'vier'