try:
  a = int(input("Dividend: "))
  b = int(input("Divisor: "))
  ergebnis = a / b
  print(f"Das Ergebnis lautet {ergebnis}")
except ValueError:
  print("Die eingegebene Zahl ist ungültig!")
print("Bye Bye!")