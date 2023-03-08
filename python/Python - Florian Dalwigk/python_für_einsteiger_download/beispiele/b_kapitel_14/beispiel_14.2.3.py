try:
  a = int(input("Dividend: "))
  b = int(input("Divisor: "))
  ergebnis = a / b
  print(f"Das Ergebnis lautet {ergebnis}")
except ZeroDivisionError: # except (ZeroDivisionError, ValueError):
  print("Es darf nicht durch 0 geteilt werden!")
except ValueError:
  print("Die eingegebene Zahl ist ungültig!")
