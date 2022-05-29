import numpy as np
from dataget import Input
from calculation import Method

class Queue:
    def __init__(self,word):
        self.name = word
        print(word)
        self.entity = Input.dataget()

def intensive():
    syntax = Input.syntaxget()
    array = Method.tostr(syntax)
    forign = []
    shuck = []
    mark = []
    for word in array:
        if mark.count(word) == 0:
            mark.append(word)
            forign.append(Queue(word))

    for word in syntax:
        if word.isalpha() == False and word.isdigit() == False:
            shuck.append(word)


    for data in forign:
        print(data.name)


intensive()
