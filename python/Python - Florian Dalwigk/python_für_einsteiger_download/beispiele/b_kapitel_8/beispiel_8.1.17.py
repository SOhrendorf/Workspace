teilnehmer = ["Max","Pia","Lea","Alf","Pia","Bea","Pia"]
wie_oft = teilnehmer.count("Pia")
print(wie_oft)
# Es wird der Wert 3 ausgegeben
wie_oft = teilnehmer.count("pia")
"""
In der Variable "wie_oft" wird der Wert 0 gespeichert, 
da "pia" nicht in der Liste vorkommt
"""