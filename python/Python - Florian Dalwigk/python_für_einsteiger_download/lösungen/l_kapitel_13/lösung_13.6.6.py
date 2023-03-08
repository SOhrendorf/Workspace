class Konto: 
  def __init__(self,kontoinhaber,kontonummer,betrag):
    self.__kontoinhaber = kontoinhaber
    self.__kontonummer = kontonummer
    self.__betrag = betrag
 
  # Methode zum Auslesen der Infos.
  def get_info(self,schlüssel):
    if schlüssel == "Kontoinhaber":
      return self.__kontoinhaber
    elif schlüssel == "Kontonummer":
      return self.__kontonummer
    else: 
      print("Es wurde keine passende Information gefunden!")