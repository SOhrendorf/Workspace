import sys
if len(sys.argv) > 1:
  name = sys.argv[1]
  print(f"Hallo {name}!")
else:
  print("Du hast keinen Namen genannt!")