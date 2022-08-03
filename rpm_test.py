class Method:
#   逆ポーランド記法への変換
    def convert_to_rpn(self,expr):
        length = len(expr)
        if length < 3:
            return expr

        if self.find_brackets(expr) == length-1:
            expr = expr[1:-1]
        
        return self.find_add_sub(self,expr) or self.find_mul(self,expr) or expr

        # 不要な括弧の検出
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

        # 演算子の検出　＋、ー
    def find_add_sub(self,expr):
        result = []
        code = []
        code_ct = 0
        deep = 0
        st = 0
        for ct, c in enumerate(expr):
            deep = self.deep_process(deep,c)
            if deep == 0:
                if c == '+' or c == '-':
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

        # 演算子の検出　＊ need to improve
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
                if c == '*':
                    st += 1

                elif ct >= len(expr)-1:
                    result.append(self.convert_to_rpn(self,expr[st:ct+1]))
                    code_ct += 1
                    st = ct + 1

                elif (( c.isdigit() or c == '-' ) and expr[ct+1].isdigit()) == False:
                    result.append(self.convert_to_rpn(self,expr[st:ct+1]))
                    code_ct += 1
                    st = ct + 1
            
                if( code_ct > 1 ):
                    result.append('*')
                    code_ct = 1
                    st = ct + 1
        return result

        # 2桁以上の数値のデータをつなげる
    def next_data(c,next_c):
        result = True
        if ( c.isdigit() or c == '-' )and next_c.isdigit():
            result = False

        return result


        # 再帰関数の深さ
    def deep_process(deep,c):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -= 1
        return deep

#   list型をstr型に
    def convert_to_str(self,list):
        array = []
        for cell in list:
            if isinstance(cell, str):
                array.append(cell)
            else:
                array += self.convert_to_str(self,cell)

        return array
data = input()
data = Method.convert_to_rpn(Method,data)
print(data)