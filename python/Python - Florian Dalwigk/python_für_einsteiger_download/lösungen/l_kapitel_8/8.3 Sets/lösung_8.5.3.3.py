gerade = {0,2,4,6,8,10}

kopie = gerade
# gerade = {0,2,4,6,8,10}

kopie.remove(4)
# gerade = {0,2,6,8,10}

kopie.add(12)
# gerade = {0,2,6,8,10,12}

kopie.add(8)
# gerade = {0,2,6,8,10,12}

print(gerade)
# Es wird das Set {0,2,6,8,10,12} ausgegeben. Beachte, dass die Reihenfolge der Elemente anders sein kann.
# Das liegt daran, dass mit = keine tiefe, sondern nur eine flache Kopie angefertigt wird.
# Mit der Methode copy kann man eine tiefe Kopie anfertigen. 

kopie = gerade.copy()