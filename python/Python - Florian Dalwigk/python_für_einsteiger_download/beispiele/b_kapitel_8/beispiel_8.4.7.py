serien = {
  "Avatar – Der Herr der Elemente" : 10,
  "Steins;Gate" : 9,
  "Sword Art Online" : 10,
  "Squid Game" : 8
}
serien.update({"Mr. Robot" : 9})
bewertung_mr_robot = serien.get("Mr. Robot")
print(bewertung_mr_robot)
# Ausgabe: 9
serien.update({"Squid Game" : 7})
print(serien.get("Squid Game"))
# Ausgabe: 7
