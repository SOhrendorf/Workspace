class Bruch:
  def __init__(self, zähler, nenner):
    self.zähler = zähler
    self.nenner = nenner
    self.__kürzen()

  def __str__(self):
    if self.zähler == 0:
      return "0"
    elif self.nenner == 0:
      return "Dieser Bruch ist nicht definiert!"
    elif self.nenner == 1:
      return str(self.zähler)
    elif (self.zähler < 0) ^ (self.nenner < 0):
      return f"-{abs(self.zähler)}/{abs(self.nenner)}"
    else:
      return f"{abs(self.zähler)}/{abs(self.nenner)}"  
  
  def __add__(self,other):
    zähler = self.zähler * other.nenner + self.nenner * other.zähler
    nenner = self.nenner * other.nenner
    return Bruch(zähler,nenner)

  def __sub__(self,other):
    zähler = self.zähler * other.nenner - self.nenner * other.zähler
    nenner = self.nenner * other.nenner
    return Bruch(zähler,nenner)
    
  def __mul__(self,other):
    zähler = self.zähler * other.zähler
    nenner = self.nenner * other.nenner
    return Bruch(zähler,nenner)
    
  def __truediv__(self,other):
    zähler = self.zähler * other.nenner
    nenner = self.nenner * other.zähler
    return Bruch(zähler,nenner)
    
  def __eq__(self,other):   
    return self.zähler == other.zähler and self.nenner == other.nenner 
    
  def __lt__(self,other):
    return self.zähler/self.nenner < other.zähler/other.nenner  
    
  def __gt__(self,other):
    return self.zähler/self.nenner > other.zähler/other.nenner
    
  def __kürzen(self):
    ggT = self.__ggt(abs(self.zähler),abs(self.nenner))
    self.zähler //= ggT
    self.nenner //= ggT
    
  def __ggt(self,x,y):
    z = x % y
    if z == 0:
      return y
    return self.__ggt(y,z)