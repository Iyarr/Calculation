
class Method:
    #   逆ポーランド記法への変換
    def porandmake(self,syntax):
        length = len(syntax)
        if length < 2:
            return syntax
        #
        ct = 0
        deep = 0
        while ct < length:
            if syntax[ct] == '(':
                deep = deep + 1
            elif syntax[ct] == ')':
                deep = deep - 1
                
            if deep == 0:
                if ct >= length-1:
                    syntax = syntax[1:length-1]
                    length = length - 2
                break
            ct = ct + 1
        #
        sign = 0
        deep = 0
        ct = 0
        while ct < length:
            if syntax[ct] == '(':
                deep = deep + 1
            elif syntax[ct] == ')':
                deep = deep - 1

            elif deep == 0:
                if syntax[ct] == '+' or syntax[ct] == '-':
                    former = self.porandmake(self,syntax[0:ct])
                    latter = self.porandmake(self,syntax[ct+1:length])
                    sign = 1
                    return [former,latter,syntax[ct]]
            ct = ct + 1
        #
        ct = 0
        if sign == 0:
            level = 0
            st = 0
            while ct < length:
                if syntax[ct] == '(':
                    deep = deep + 1

                elif syntax[ct] == ')':
                    deep = deep - 1
                    if deep == 0:
                        level = level + 1
                        if level == 1:
                            st = ct
                        
                elif deep == 0 :
                    if ct + 1 < length and syntax[ct].isdigit():
                        if syntax[ct+1].isdigit() == False:
                            level = level + 1
                            if level == 1:
                                st = ct
                    else :
                        level = level + 1
                        if level == 1:
                            st = ct


                if level == 2:
                    former = self.porandmake(self,syntax[0:st+1])
                    latter = self.porandmake(self,syntax[st+1:length])
                    return [former,latter,'*']
                ct = ct + 1
        return syntax
        
    def tostr(self,syntax):
        array = ''
        for cell in syntax:
            length = len(cell)
            if length == 1 :
                if cell.isalpha():
                    array = array + cell
            elif length > 1:
                array = array + self.tostr(cell)
        return array