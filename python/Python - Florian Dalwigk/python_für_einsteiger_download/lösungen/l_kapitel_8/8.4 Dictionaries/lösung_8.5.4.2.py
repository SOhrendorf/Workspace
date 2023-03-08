zahlen = {"eins" : 1, "zwei" : 2, "drei" : 3}   # {"eins" : 1, "zwei" : 2, "drei" : 3}
zahlen.update({"eins" : 2})                     # {"eins" : 2, "zwei" : 2, "drei" : 3}
del zahlen["drei"]                              # {"eins" : 2, "zwei" : 2}
zahlen.clear()                                  # {}
zahlen.update({"null" : 0})                     # {"null" : 0}
zahlen.update({"eins" : 0})                     # {"null" : 0, "eins" : 0}
zahlen["eins"] = 1                              # {"null" : 0, "eins" : 1}
del zahlen["null"]                              # {"eins" : 0}