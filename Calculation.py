import math
import numpy as np

class mathod:
    def __init__(self,myname,syntax):
        self.name = myname
        self.values = self.porandmake(self,syntax)
        pass
    #   逆ポーランド記法への変換
    def porandmake(self,syntax):
        syntax = self.__trip(syntax)
        length = len(syntax)
        deep = 0
        ct = 0
        entity = self.__separate(syntax)
        tree = []*3

        tree[0] = entity[0]

        tree[1] = self.porandmake(entity[1])
        tree[2] = self.porandmake(entity[2])

        syntax = tree[1]+tree[2]+tree[0]

        return syntax

    def __trip(self,syntax):
        ct = 0
        for word in syntax :
            last = word
            if word == '(':
                deep = deep + 1

            elif word == ')':
                deep = deep - 1
                
            if deep == 0:
                if ct < len(syntax):
                    return syntax
                else:
                    return syntax[1:len(syntax)-1]
            
            ct=ct+1

        return syntax

    def __separate(self,syntax):
        length = len(syntax)
        entity = []*3
        sign = 0
        ct = 0
        while(ct < length):
            if syntax[ct] == '(':
                deep = deep + 1

            elif syntax[ct] == ')':
                deep = deep - 1

            elif deep == 0:
                if syntax[ct] == '+':
                    syntax[ct] = ' '
                    return np.array('+',syntax.split(' ',0),syntax.split(' ',1))
                elif syntax[ct] == '-':
                    syntax[ct] = ' '
                    return np.array('-',syntax.split(' ',0),syntax.split(' ',1))

        return self.__intergral(self,syntax)
        
    # insert *
    def __intergral(self,syntax):
        length = len(syntax)
        ctin = 0
        ctout = 0
        while ctin < length:
            ctout = ctout + 1
            if syntax[ctin] == '(':
                init = ctin
                deep = 0
                while syntax[ctin] !=  ')' | deep != 0:
                    if syntax[ctin] ==  '(':
                        deep = deep + 1

                    elif syntax[ctin] ==  ')':
                        deep = deep - 1

                    ctin = ctin + 1
                syntax = syntax[0:init-1]+self.porandmake(syntax[init:len-1])
                
            if ctout >= 2:
                syntax = syntax[0:ctin] + '*' + syntax[ctin:len-1]
                ctout = 1
                ctin = ctin + 1
                length = length + 1
            ctin = ctin + 1

        return syntax

    #   alternative input process
    def syntaxget(self):
        syntax = input("式を入力してください")
        syntax = syntax.replace(' ','')
        syntax = syntax.replace('*', '')
        length = len(syntax)
        syntax = self.porandmake(syntax)

        return syntax
