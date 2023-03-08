try:
  a = int(input("Dividend: "))
  b = int(input("Divisor: "))
  ergebnis = a / b
  print(f"Das Ergebnis lautet {ergebnis}")
except (ZeroDivisionError, ValueError):
  print(f"Es ist ein Fehler aufgetreten!")
else:
  print("Es ist kein Fehler aufgetreten!")