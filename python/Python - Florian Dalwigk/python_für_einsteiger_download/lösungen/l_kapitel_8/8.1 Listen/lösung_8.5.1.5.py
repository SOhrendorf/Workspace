buchstaben = ['A','B','C','D','E']

kopie = buchstaben
# buchstaben = ['A','B','C','D','E']

kopie[2] = 'F'
# buchstaben = ['A','B','F','D','E']

kopie.append('G')
# buchstaben = ['A','B','F','D','E','G']

kopie.remove('A')
# buchstaben = ['B','F','D','E','G']

print(buchstaben)
# Es wird die Liste ['B','F','D','E','G'] ausgegeben. 
# Das liegt daran, dass mit = keine tiefe, sondern nur eine flache Kopie angefertigt wird.
# Mit der Methode copy kann man eine tiefe Kopie anfertigen. 

kopie = buchstaben.copy()