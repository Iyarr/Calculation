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
    def __init__(self,str):
        self.compose = [0]*26
        self.number = 1
        self.mul_data(self,str)

    def mul_data(self,str):
        if str.isdigit() == True:
            self.number = self.number * int(str)

        else:
            for ct_str in range(26):
                if str == string.ascii_letters[ct_str]:
                    self.compose[ct_str] += 1
                    break