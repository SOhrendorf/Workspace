import sys

try:
  a = int(input("Dividend: "))
  b = int(input("Divisor: "))
  ergebnis = a / b
  print(f"Das Ergebnis lautet {ergebnis}")
except ZeroDivisionError:
  print("Es darf nicht durch 0 geteilt werden!")
except:  
  error = sys.exc_info()[0]
  print(f"Es ist ein {error} aufgetreten!")