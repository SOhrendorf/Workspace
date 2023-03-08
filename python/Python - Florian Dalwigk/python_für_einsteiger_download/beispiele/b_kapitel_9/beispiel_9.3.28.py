namen = ["Chan", "Kevin", "Mayu", "Haruka"]
print([(name,i) for i,name in enumerate(namen)])
# Ausgabe: [("Chan",0), ("Kevin",1), ("Mayu",2), ("Haruka",3)]
print([(i,2*i) for i,name in enumerate(namen)])
# Ausgabe: [(0, 0), (1, 2), (2, 4), (3, 6)]