bits = [1,0,1]
print(bits * 3)
# Die Ausgabe lautet [1,0,1,1,0,1,1,0,1] 
print(3 * bits)
# Die Ausgabe lautet erneut [1,0,1,1,0,1,1,0,1]
print(3 * [1,0,1])
# Die Ausgabe lautet auch hier [1,0,1,1,0,1,1,0,1]
bits * bits # TypeError: can't multiply sequence by non-int of type 'list'