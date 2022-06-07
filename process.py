import numpy
import string
from dataget import Input
from calculation import Method

class Queue:
    def __init__(self,word):
        self.name = word
        print(word)
        self.entity = Input.get_formula()
#　項の中身(名前、項)
class Item:
    def __init__(self,name,str):
        self.name = name
        self.compose = [0]*52
        self.number = 1
        length = len(str)
        ct = 0
        while ct < length:
            num_str = ''
            if str[ct].isdisit == True:
                num_str = ''
                while str[ct].isdisit == True:
                    num_str = num_str + str[ct]
                    ct = ct + 1
                ct = ct - 1
                self.number = self.number * int(num_str)

            else:
                ct_str = 0
                while ct_str < 52:
                    if str[ct] == string.ascii_letters[ct_str]:
                        self.compose[ct_str] = self.compose[ct_str] + 1
                        break
                    ct_str = ct_str  + 1

            ct = ct + 1
        

def intensive():
    syntax = Input.get_formula()
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
