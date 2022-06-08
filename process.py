import numpy
import string
from dataget import Input
from calculation import Method

class Queue:
    def __init__(self,word):
        self.name = word
        print(word)
        self.entity = Input.get_expr()
#　項の中身(名前、項)
class Item:
    def __init__(self,name,str):
        self.name = name
        self.compose = [0]*52
        self.number = 1
        for ct, c in str:
            if c.isdisit == True:
                num_str = ''
                while c.isdisit == True:
                    num_str += c
                    ct += 1
                ct -= 1
                self.number = self.number * int(num_str)

            else:
                for ct_str in range(52):
                    if c == string.ascii_letters[ct_str]:
                        self.compose[ct_str] += 1
                        break

def intensive():
    expr = Input.get_expr()
    array = Method.tostr(expr)
    forign = []
    shuck = []
    mark = []
    for word in array:
        if mark.count(word) == 0:
            mark.append(word)
            forign.append(Queue(word))

    for word in expr:
        if word.isalpha() == False and word.isdigit() == False:
            shuck.append(word)

    for data in forign:
        print(data.name)


intensive()
