import string

#　項の中身(名前、項)
class Item:
    def __init__(self,str,deep):
        self.compose = [0]*52
        self.number = 1
        self.deep = deep
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
    def realnum_mixed_calculator(queue,num,code):
        row_ct = len(queue)
        column_ct = len(queue[0])
        result = ['']*row_ct*column_ct
        
        for row in range(row_ct):
            result[row] = ['']*column_ct
            for column in range(column_ct):
                result[row][column] = '(' + queue[row][column] + ')' + code + num
                result[row][column] = compile(Method,Method.convert_to_rpn(Method,result[row][column]))
        return result

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
                result[common][column_ct] = compile(Method,Method.convert_to_rpn(Method,result[common][column_ct][1:]))
            
        return result
    
    def compile(exper):
        item_list = []
        deep_ct = 0
        deep_st = [0]
        for ct,c in enumerate(exper):
            if c in '+-':
                for item in reversed(item_list):
                    if item.deep != deep_ct:
                        break
                    
                    if c == '-':
                        item.mul_data('-1')

                    item.deep -= 1
                
                deep_ct -= 1

            elif c == '*':
                for item in item_list[:-2]:
                    item.mul_data(item_list[-1])
            #　演算子じゃなかったらもう項を製作する
            else :
                item_list.append(Item(c,deep_ct))
                if( deep_ct > 1 ):
                    deep_ct = 1
                    deep_st += 1
        result = ''
        for item in item_list:
            if item.number > 0:
                result += '+'
            result += item.number
            for ct,values in enumerate(item.compose):
                if values != 0:
                    result += string.ascii_letters[ct]*values
            
        return result
    #　リストの中だけに着目して計算する関数
    def compile_recursive(exper,deep):

        return exper
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
                    deep -= 1
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
        
    def convert_to_str(self,list):
        array = []
        for cell in list:
            if isinstance(cell, str):
                array.append(cell)

            else:
                array += self.convert_to_str(self,cell)

        return array
    
fomula = input("式を入力してください")
#print(Method.convert_to_rpn(Method,fomula))
print(Method.convert_to_str(Method,Method.convert_to_rpn(Method,fomula)))