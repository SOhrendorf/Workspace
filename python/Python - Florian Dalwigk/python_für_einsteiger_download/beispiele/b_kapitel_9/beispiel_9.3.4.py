text = "ich bin ein programmierer"
statistik = {}
for zeichen in text:
  if zeichen in statistik:
    statistik[zeichen] += 1
  else:
    statistik[zeichen] = 1
print(statistik)