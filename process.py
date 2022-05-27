import numpy as np
from dataget import Input
#from calculation import Method

class Queue:
    def __init__(self,word):
        self.name = word
        print(word)
        self.entity = Input.dataget()

def intensive():
    syntax = Input.syntaxget()
    array = tostr(syntax)
    forign = []
    mark = []
    for word in array:
        if mark.count(word) == 0:
            mark.append(word)
            forign.append(Queue(word))

    for data in forign:
        print(data.name)

def tostr(syntax):
    array = ''
    for cell in syntax:
        length = len(cell)
        if length == 1 :
            if cell.isalpha():
                array = array + cell
        elif length > 1:
            array = array + tostr(cell)
    return array

intensive()
