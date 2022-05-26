import numpy as np
from dataget import Input
#from calculation import Method

class Queue:
    def __init__(self,word):
        self.name = word
        self.entity = Input.dataget()

def intensive():
    syntax = Input.syntaxget()
    array = tracking(syntax)
    mark = []
    for word in array:
        if mark.count(word) == 0:
            mark.append(word)
    print(mark)

def tracking(syntax):
    array = []
    for ct in range(3):
        length = len(syntax[ct])
        if length == 1 :
            if str(syntax[ct]).isalpha():
                array = array.append(syntax[ct])
        elif length > 1:
            array = tracking(syntax[ct])

    return array

def test():
    entity = Queue('a')
    print(entity.name)

intensive()
