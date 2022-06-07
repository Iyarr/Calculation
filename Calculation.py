
class Method:
    #　逆ポーランド記法への変換
    def convert_formula_to_rpn(self,formula):
        length = len(formula)
        if length < 2:
            return formula
        
        ct = 0
        deep = 0

        #　不要な括弧の除去
        while ct < length:
            if formula[ct] == '(':
                deep = deep + 1
            elif formula[ct] == ')':
                deep = deep - 1
                
            if deep == 0:
                if ct >= length-1:
                    formula = formula[1:length-1]
                    length = length - 2
                break
            ct = ct + 1
        
        sign = 0
        deep = 0
        ct = 0
        #　演算子の検出　＋、ー
        while ct < length:
            if formula[ct] == '(':
                deep = deep + 1
            elif formula[ct] == ')':
                deep = deep - 1

            elif deep == 0:
                if formula[ct] == '+' or formula[ct] == '-':
                    former = self.porandmake(self,formula[0:ct])
                    latter = self.porandmake(self,formula[ct+1:length])
                    sign = 1
                    return [former,latter,formula[ct]]
            ct = ct + 1
        
        #　演算子の検出　＊
        if sign == 0:
            level = 0
            st = 0
            ct = 0
            while ct < length:
                if formula[ct] == '(':
                    deep = deep + 1

                elif formula[ct] == ')':
                    deep = deep - 1
                    if deep == 0:
                        level = level + 1
                        if level == 1:
                            st = ct
                        
                elif deep == 0 :
                    if ct + 1 < length and formula[ct].isdigit():
                        if formula[ct+1].isdigit() == False:
                            level = level + 1
                            if level == 1:
                                st = ct
                    else :
                        level = level + 1
                        if level == 1:
                            st = ct


                if level == 2 :
                    former = self.convert_formula_to_rpn(self,formula[0:st+1])
                    latter = self.convert_formula_to_rpn(self,formula[st+1:length])
                    return [former,latter,'*']
                elif formula[ct] == '*':
                    former = self.convert_formula_to_rpn(self,formula[0:ct])
                    latter = self.convert_formula_to_rpn(self,formula[ct+1:length])
                    return [former,latter,'*']
                ct = ct + 1
        return formula
        
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