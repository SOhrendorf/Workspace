wörterbuch = {
  "Apfel" : "apple",
  "Computer" : "computer",
  "Geld" : "money"
}
geld_englisch = wörterbuch["Geld"]
print(geld_englisch)
# Ausgabe: "money"
wörterbuch["Fenster"] # KeyError: 'Fenster'