# Definition einer Liste, in der die ausgelesenen Pokémon gespeichert werden sollen.
pokemon = []

# Datei mithilfe des Kontextmanagers im Lesemodus "r" öffnen.
with open("pokemon.txt", "r") as f:

  # Zuerst wird der gesamte Dateiinhalt mit read() ausgelesen.
  # Danach wird mit splitlines an dem Zeilenumbruch \n gesplittet, wodurch dieser verschwindet.
  # Das Ergebnis wird der zuvor definierten Liste zugewiesen.
  pokemon = f.read().splitlines()