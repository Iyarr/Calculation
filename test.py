import string
from calculation import Method


#　項の中身(名前、項)
class Item:
    def __init__(self,str):
        self.compose = [0]*52
        self.number = 1
        self.mul_data(self,str)

    def mul_data(self,str):
        if str.isdigit() == True:
            self.number = self.number * int(str)

        else:
            for ct_str in range(52):
                if str == string.ascii_letters[ct_str]:
                    self.compose[ct_str] += 1
                    break
def compile(exper):
        item_list = []
        for c in exper:
            if c == '-':
                item_list[-1].mul_data('-1')
            elif c == '*':
                for item in item_list[:-2]:
                    item.mul_data(item_list[-1])
            elif c.isalpha():
                item_list.append(Item(c))
        result = ''
        for item in item_list:
            if item.number > 0:
                result += '+'
            result += item.number
            for ct,values in item.compose:
                if values != 0:
                    result += string.ascii_letters[ct]*values
            
        return result
formula = input("式を入力")
print(compile(Method.convert_to_list(Method,Method.convert_to_rpn(Method,formula))))