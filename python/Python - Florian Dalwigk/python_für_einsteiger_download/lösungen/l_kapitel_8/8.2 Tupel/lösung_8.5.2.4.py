def rechnen(a,b):
  return a+b, a-b, a*b, a/b

# Es werden vier Ergebnisse zurückgegeben, d.h. wir benötigen vier Variablen.
# Diese nennen wir summe, differenz, produkt und quotient, weil es das ist, was berechnet wird.

summe, differenz, produkt, quotient = rechnen(6,3)

# Die Ergebnisse lauten: 
print(f"a+b={summe}\na-b={differenz}\na*b={produkt}\na/b={quotient}\n")