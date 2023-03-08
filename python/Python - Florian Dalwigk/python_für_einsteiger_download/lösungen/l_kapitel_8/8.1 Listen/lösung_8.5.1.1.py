daten = ["abc123",12,True,0.25,-3,'J','N']
daten[0]        # "abc123"
daten[3]        # 0.25
daten[-2]       # 'J' -> Wir starten von hinten ('N' = Index -1)
daten[-5]       # True -> Wir starten von hinten ('N' = Index -1)
daten[2]        # True
daten[2+2]      # -3 -> Der Index ist 4. 
daten[3*0-1]    # 'N' -> Der Index ist -1. Wir starten von hinten ('N' = Index -1)
daten[3//3]     # 12 -> Der Index ist 1
daten[-1*3]     # -3 -> Der Index ist -3. Wir starten von hinten ('N' = Index -1)
daten[7-2]      # 'J' -> Der Index ist 5.
