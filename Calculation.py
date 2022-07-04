import string

#　項の中身(名前、項)
class Item:
    def __init__(self,str):
        if str[0] == '-':
            self.number = -1
        else:
            self.number = 1
        self.compose = [0]*52
        switch = 0
        num = ''
        for c in str:
            if c.isdigit() == False:
                switch = 1
            
            if switch == 0:
                num = num + c

            else:
                for ct_str in range(52):
                    if str == string.ascii_letters[ct_str]:
                        self.compose[ct_str] += 1
                        break
        if len(num) > 0:
            self.number *= int(num)
    
class Method:
    def realnum_mixed_calculator(queue,num,code):
        row_ct = len(queue)
        column_ct = len(queue[0])
        result = ['']*row_ct*column_ct
        
        for row in range(row_ct):
            result[row] = ['']*column_ct
            for column in range(column_ct):
                result[row][column] = '(' + queue[row][column] + ')' + code + num
                result[row][column] = compile(Method.convert_to_rpn(Method,result[row][column]))
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
                result[common][column_ct] = compile(Method.convert_to_rpn(Method,result[common][column_ct][1:]))
            
        return result
    
    def compile(exper):
        if len(exper) < 3:
            return exper
        elif exper[2].isdigit() == True or exper[2].isalpha() == True:
            return exper
        
        # それぞれ普通の計算式が来たと仮定する
        former = compile(exper[0])
        latter = compile(exper[1])
        code = exper[2]
 
        if code == '+':
            if former.isdigit() == True and latter.isdigit() == True:
                return str(int(former)+int(latter))
            
            if latter[0] == '-':
                return former+latter
            
            return former+'+'+latter

        if code == '-':
            if former.isdigit() == True and latter.isdigit() == True:
                return str(int(former)-int(latter))
            
            if latter[0] != '-':
                latter = '+'+latter
            return former + latter.replace('-','*').replace('+','-').replace('*','+')
            
        if code == '*':
            result = ''
            for former_pertition in former.replace('+','*+').replace('-','*-').split('*'):
                for latter_pertition in latter.replace('+','*+').replace('-','*-').split('*'):
                    result = result + Method.mul_cal(former_pertition,latter_pertition)

            return result
        return exper
    #　リストの中だけに着目して計算する関数
    def mul_cal(former,latter):
        former_item = Item(former)
        latter_item = Item(latter)
        result = str(former_item.number * latter_item.number)
        for ct_str in range(52):
            former_item.compose[ct_str] += latter_item.compose[ct_str]
            for log in range(former_item.compose[ct_str]):
                result = result + string.ascii_letters[ct_str]
        
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
        result = []
        code = []
        code_ct = 0
        deep = 0
        st = 0
        if expr == '-':
            code_ct = 1
        for ct, c in enumerate(expr):
            deep = self.deep_process(deep,c)
            if deep == 0:
                if c in '+-':
                    result.append(self.convert_to_rpn(self,expr[st:ct]))
                    code.append(c)
                    code_ct += 1
                    if code_ct >= 2:
                        result.append(code[0])
                        code.pop(0)
                        code_ct = 1
                    st = ct + 1
        
        if len(result) < 1:
            return None

        result.append(self.convert_to_rpn(self,expr[st:]))
        result.append(code[-1])
        return result

        #　演算子の検出　＊
    def find_mul(self,expr):
        if len(expr) < 2:
            return None
        result = []
        code_ct = 0
        deep = 0
        st = 0
        for ct, c in enumerate(expr):
            deep = self.deep_process(deep,c)
            if deep == 0:
                if self.data_spices(expr,ct) < 2:
                    result.append(self.convert_to_rpn(self,expr[st:ct+1]))
                    code_ct += 1
                    if( code_ct > 1 ):
                        result.append('*')
                        code_ct = 1
                    st = ct+1
        return result

        #　2桁以上の数値のデータをつなげる
    def data_spices(expr,ct):
        result = 0
        if ct < len(expr)-1:
            for data in [expr[ct],expr[ct+1]]:
                if data == '-' or data.isdigit() == True:
                    result += 1
        return result

        #　再帰関数の深さ
    def deep_process(deep,c):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -= 1
        return deep
        
    def convert_to_str(self,list):
        array = []
        for cell in list:
            if isinstance(cell, str):
                array.append(cell)

            else:
                array += self.convert_to_str(self,cell)

        return array