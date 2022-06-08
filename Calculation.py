
class Method:
#   逆ポーランド記法への変換
    def convert_to_rpn(self,expr):
        length = len(expr)
        if length < 2:
            return expr

        if self.find_brackets(expr) == length-1:
            expr = expr[1:-1]
        
        return self.find_add_sub(expr) or self.find_mul(expr) or expr

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
                    return [self.convert_to_rpn(expr[:ct]),self.convert_to_rpn(expr[ct+1:]),c]
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
                    return [self.convert_to_rpn(expr[:ct]),self.convert_to_rpn(expr[ct+1:]),'*']
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
                return [self.convert_to_rpn(expr[:st+1]),self.convert_to_rpn(expr[st+1:]),'*']
        return None
        
    def tostr(self,list):
        array = ''
        for cell in list:
            length = len(cell)
            if length == 1 :
                if cell.isalpha():
                    return cell
            elif length > 1:
                return array + self.tostr(self,cell)
        return array