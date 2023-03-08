note = input("Gib eine Schulnote von 1 bis 6 ein: ")
match note:
  case "1":
    print("sehr gut")
  case "2":
    print("gut")
  case "3":
    print("befriedigend")
  case "4":
    print("ausreichend")
  case "5":
    print("mangelhaft")
  case "6":
    print("ungenügend")
  case _:
    print("Es konnte keine passende Note ermittelt werden.")