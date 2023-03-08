zahlen = {1,0}      # 2     {1,0}
zahlen.clear()      # 0     set() <- Das ist das leere Set
zahlen.add(3)       # 1     {3}
zahlen.add(2)       # 2     {3,2}
zahlen.add(3)       # 2     {3,2}
zahlen.remove(3)    # 1     {2}
zahlen.add(2)       # 1     {2}
zahlen.add(0)       # 2     {2,0}
zahlen.add(1)       # 3     {2,0,1}
zahlen.add(1)       # 3     {2,0,1}
zahlen.remove(2)    # 2     {0,1}