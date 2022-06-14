import string

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
class Method:
    
    def calculator(former,latter,code):
        row_ct = len(former)
        column_ct = len(latter[0])
        common_ct = len(latter)
        result = ['']*row_ct*column_ct
        for row in range(row_ct):
            result[row] = ['']*column_ct
            for column in range(column_ct):
                for common in range(common_ct):
                    result[common][column_ct] += '+'+'('+former[row][common_ct]+')'+code+'('+latter[common_ct][column]+')'
                result[common][column_ct] = Method.convert_to_rpn(Method,result[common][column_ct][1:])

        return compile(Method.convert_to_list(Method,result))
    
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
            for ct,values in enumerate(item.compose):
                if values != 0:
                    result += string.ascii_letters[ct]*values
            
        return result
#   逆ポーランド記法への変換
    def convert_to_rpn(self,expr):
        length = len(expr)
        if length < 2:
            return expr

        if self.find_brackets(expr) == length-1:
            expr = expr[1:-1]
        
        return self.find_add_sub(self,expr) or self.find_mul(self,expr) or expr

        #　不要な括弧の検出
    def find_brackets(expr):
        deep = 0
        for ct, c in enumerate(expr):
            if c == '(':
                deep += 1
            elif c == ')':
                deep -= 1

            if deep == 0:
                break

        return ct

        #　演算子の検出　＋、ー
    def find_add_sub(self,expr):
        deep = 0
        for ct, c in enumerate(expr):
            if c == '(':
                deep += 1
            elif c == ')':
                    deep += 1
            elif deep == 0:
                if c in '+-':
                    return [self.convert_to_rpn(self,expr[:ct]),self.convert_to_rpn(self,expr[ct+1:]),c]
        return None

        #　演算子の検出　＊
    def find_mul(self,expr):
        length = len(expr)
        level = 0
        deep = 0
        for ct, c in enumerate(expr):
            if c == '(':
                deep += 1
            elif c == ')':
                deep -=  1

            if deep == 0:
                if c == '*':
                    return [self.convert_to_rpn(self,expr[:ct]),self.convert_to_rpn(self,expr[ct+1:]),'*']
                if ct + 1 < length and c.isdigit():
                    if expr[ct+1].isdigit() == False:
                        level += 1
                        if level == 1:
                            st = ct
                else :
                    level += 1
                    if level == 1:
                        st = ct
            if level == 2:
                return [self.convert_to_rpn(self,expr[:st+1]),self.convert_to_rpn(self,expr[st+1:]),'*']
        return None
        
    def convert_to_list(self,list):
        array = []
        for cell in list:
            length = len(cell)
            if length <= 1 or cell.isdigit():
                array.append(cell)
            elif length > 1:
                return array + self.convert_to_list(self,cell)
        return array