import string

#　項の中身(名前、項)
class Item:
    def __init__(self,str):
        if str[0] == '-':
            self.number = -1
            str = str[1:]
        else:
            self.number = 1
        self.compose = [0]*26
        switch = 0
        for c in str:
            if c.isdigit() == False:
                if switch == 1:
                    self.number *= int(num)
                switch = 0
            else:
                if switch == 0:
                    switch = 1
                    num = ''

            if switch == 1:
                num = num + c
            else:
                for ct_str in range(26):
                    if c == string.ascii_letters[ct_str]:
                        self.compose[ct_str] += 1
                        break
        if switch == 1:
            self.number *= int(num)
class Method:
    def realnum_mixed_calculator(self,queue,num,code):
        row_ct = len(queue)
        column_ct = len(queue[0])
        result = ['']*row_ct*column_ct
        
        for row in range(row_ct):
            result[row] = ['']*column_ct
            for column in range(column_ct):
                result[row][column] = self.compile([result[row][column],num,code])
        return result

    def calculator(self,former,latter,code):
        row_ct = len(former)
        column_ct = len(latter[0])
        common_ct = len(latter)
        result = []*row_ct*column_ct
        for row in range(row_ct):
            result[row] = ['0']*column_ct
            for column in range(column_ct):
                for common in range(common_ct):
                    result[common][column_ct] = [result[common][column_ct],[former[row][common_ct],latter[common_ct][column],code],'+']
                result[common][column_ct] = self.compile(result[common][column_ct])
            
        return result
    
    def compile(self,exper):
        if len(exper) < 3:
            return exper

        # それぞれ普通の計算式が来たと仮定する
        stuck = []
        for partition in exper:
            if  isinstance(partition,list):
                stuck.append(compile(partition))

            elif partition == '+'or partition == '-':
                stuck[-2] = self.add_cal(self,stuck[-2],stuck[-1],partition)
                stuck.pop(-1)

            elif partition == '*':
                stuck[-2] = self.mul_cal(self,stuck[-2],stuck[-1])
                stuck.pop(-1)

            else:
                stuck.append(self.compile(self,partition))

        return stuck[0]

    def mul_cal(self,former,latter):
        result= ''
        former = former[0] + former[1:].replace('+','/').replace('-','/-')
        latter = latter[0] + latter[1:].replace('+','/').replace('-','/-')
        for former_c in former.split('/'):
            if former_c[0] == '-':
                former_code = 'minus'
                former_c = former_c[1:]
            else:
                former_code = 'plus'

            for latter_c in latter.split('/'):
                if latter_c[0] == '-':
                    latter_code = 'minus'
                    latter_c = latter_c[1:]
                else:
                    latter_code = 'plus'

                if former_code != latter_code:
                    result += '-'
                else:
                    result += '+'

                if former_c[-1].isdigit() and ( latter_c[0].isdigit() or latter_c[:1].isdigit() ):
                    result += former_c + '|' + latter_c
                else:
                    result += former_c + latter_c

        return self.cleaner(result)

    def add_cal(self,former,latter,code):

        if latter[0] != '-':
            latter = '+' + latter

        if code == '+':
            result = former + latter

        else:
            result = former + latter.replace('+','/').replace('-','+').replace('/','-')

        return self.cleaner(result)

    def cleaner(exper):
        exper = exper[0] + exper[1:].replace('+','/').replace('-','/-')
        inventory = []
        for data in exper.split('/'):
            current = Item(data)
            identical = 0
            if len(inventory) > 0:
                for ct,comparison in enumerate(inventory):
                    for ct_str in range(26):
                        if current.compose[ct_str] != comparison.compose[ct_str]:
                            break
                    if ct_str == 25:
                        inventory[ct].number += current.number
                        identical = 1
                        break

            if identical == 0:
                inventory.append(current)

        result = ''
        for comparison in inventory:
            if comparison.number > 0 :
                result += '+'
                if comparison.number != 1:
                    result += str(comparison.number)
            elif comparison.number != 0:
                result += '-'
                if comparison.number != -1:
                    result += str( -1 * comparison.number)
            else:
                continue

            for ct_str in range(26):
                result += string.ascii_letters[ct_str]*comparison.compose[ct_str]

        if result[0] == '+':
            result = result[1:]

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
        code_ct = deep = st = 0
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

        return result.append(self.convert_to_rpn(self,expr[st:])).append(code[-1])

        #　演算子の検出　＊

    def find_mul(self,expr):
        if len(expr) < 2:
            return None
        result = []
        code_ct = deep = st = 0
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

        #　2桁以上の数値のデータをつなげる
    def next_data(c,next_c):
        result = True
        if ( c.isdigit() or c == '-' )and next_c.isdigit():
            result = False

        return result

        #　再帰関数の深さ
    def deep_process(deep,c):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -= 1
        return deep

        #  list型をstr型に
    def convert_to_str(self,list):
        array = []
        for cell in list:
            if isinstance(cell, str):
                array.append(cell)
            else:
                array += self.convert_to_str(self,cell)

        return array