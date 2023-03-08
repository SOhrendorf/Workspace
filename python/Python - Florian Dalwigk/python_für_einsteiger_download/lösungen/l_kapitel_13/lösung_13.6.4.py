class Konto: 
  def __init__(self,kontoinhaber,kontonummer,betrag):
    self.__kontoinhaber = kontoinhaber
    self.__kontonummer = kontonummer
    self.__betrag = betrag
    
  def abheben(self,betrag):
    if self.__betrag - betrag < 0:
      print("Der Betrag kann nicht abgehoben werden.")
    else:
      self.__betrag -= betrag
      print(f"Es wurden {betrag}€ abgehoben.")
      print(f"Aktueller Kontostand: {self.__betrag}€")
      
  def einzahlen(self,betrag):
    if betrag > 0:
      self.__betrag += betrag
      print(f"Es wurden {betrag}€ eingezahlt.")
      print(f"Aktueller Kontostand: {self.__betrag}€")
    else:
      print("Es kann kein negativer Betrag eingezahlt werden.")

  # Hierfür verwenden wir die magische Methode "__eq__".
  def __eq__(self,other):
    # Wir verknüpfen alle Vergleiche der Objektvariablen mit einem logischen "und" und geben das Ergebnis zurück.
    return self.__kontoinhaber == other.__kontoinhaber and self.__kontonummer == other.__kontonummer and self.__betrag == other.__betrag