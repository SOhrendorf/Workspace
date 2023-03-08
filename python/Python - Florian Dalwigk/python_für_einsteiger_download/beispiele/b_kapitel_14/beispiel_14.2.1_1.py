try:
  a = int(input("Dividend: "))
  b = int(input("Divisor: "))
  ergebnis = a / b
  print(f"Das Ergebnis lautet {ergebnis}")
except ZeroDivisionError:
  print("Es darf nicht durch 0 geteilt werden!")
print("Bye Bye!")