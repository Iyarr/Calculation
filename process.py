import numpy as np
from dataget import Input
#from calculation import Method

class Queue:
    def __init__(self,word):
        self.name = word
        self.entity = []
        self.entity = Input.dataget()

def intensive():
    syntax = Input.syntaxget()
    mark = syntax.flatten()
    print(mark)
    for word in mark:
        if word.isalpha() == True:
            mark.append(word)
    print(mark)
    length = len(mark)
    ct = 0
    while ct < length:
        ct = ct + 1
def test():
    entity = Queue('a')
    print(entity.name)

intensive()
