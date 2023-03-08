a = "Buchhaltung"
b = "Python ist toll!"

print(a[5])                             # "a"
print(b[-1])                            # "!", weil von hinten begonnen wird.
print(a[:4])                            # "Buch" - Der Startindex ist 0, weil vor dem Doppelpunkt kein Index steht.
print(b[11:16])                         # "toll!"
print(a[-100:100])                      # "Buchhaltung" - Alles wird ausgegeben, weil -100 und 100 außerhalb der maximalen Indizes liegt.
print(b.index('o'))                     # 4
print("Maximilian".index('x'))          # 2
print("123456789".index('5'))           # 4, weil bei 0 zu zählen begonnen wird
print(b.replace("ist","ist super"))     # "Python ist super toll!" - "ist" wird durch "ist super" ersetzt.
print(".....".replace('.','*'))         # "*****" 