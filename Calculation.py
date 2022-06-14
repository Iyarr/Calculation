from make_data import Item

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

        return compile(result)
    
    def compile(exper):

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
            if length <= 1 or cell.isdisit():
                array.append(cell)
            elif length > 1:
                return array + self.convert_to_list(self,cell)
        return array