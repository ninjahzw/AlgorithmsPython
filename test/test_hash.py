__author__ = "zhaowei"
__author__ = "mark"
class test:
    
    def __init__(self):
        return

    def __hash__(self):
        return hash('test') 

t = (test(), 'a', 1)
print (hash(t))
