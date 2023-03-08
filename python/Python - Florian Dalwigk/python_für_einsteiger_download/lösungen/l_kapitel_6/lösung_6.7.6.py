# Nicht möglich, weil **c vor *d steht.
def f(a, b,**c,*d): 

# Nicht möglich, weil der Parameter x zweimal verwendet wird.
def dividieren(x,x):

# Nicht möglich, weil "Tim" kein Variablenname ist.
def sag_hallo("Tim", nachname):

# Möglich.
def einkaufen(**produkte):

# Möglich.
def f(x=3):

# Nicht möglich, weil *empfaenger kein einzelner String zugewiesen werden kann. Es handelt sich um einen *args-Parameter.
def ueberweisen(sender, *empfaenger="Rintaro"):

# Möglich.
def email_senden(sender, empfaenger="info@example.com"):

# Möglich.
def f(x=1, y, z, *params1, **params2):
