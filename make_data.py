import string
from calculation import Method

class Input:
    def get_queue():
        queue = []
        while(1):
            row = input()
            if( row == ''):
                break
            queue.append(row.split(" "))
        return queue

    def get_expr():
        return Method.convert_to_rpn(Method,input("式を入力してください\n").replace(' ',''))

class Queue:
    def __init__(self,word):
        self.name = word
        print(word+"に対応する行列を入力してください\n")
        self.entity = Input.get_queue()

#　項の中身(名前、項)
class Item:
    def __init__(self,name,str):
        self.name = name
        self.compose = [0]*52
        self.number = 1
        for ct, c in str:
            if c.isdigit() == True:
                num_str = ''
                while c.isdigit() == True:
                    num_str += c
                    ct += 1
                ct -= 1
                self.number = self.number * int(num_str)

            else:
                for ct_str in range(52):
                    if c == string.ascii_letters[ct_str]:
                        self.compose[ct_str] += 1
                        break