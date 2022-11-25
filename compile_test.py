import string
import re
from rpm_test import Method
class Item:     #　項の中身(名前、項)
    def __init__(self,item):
        self.number = 1
        if item[0] == '-':
            self.number = -1
            item = item[1:]
        borderline = len(re.split('*[0-9]',item,1)[1])+1    #正規表現で左側の数字の文字列の長さを検出して格納する
        self.alphabet_compose = item[borderline:].sorted()
        if borderline > 0:
            self.number *= int(item[:borderline])

class cal:
    def compile(self,exper):
        if isinstance(exper,str) or len(exper) == 0:
            return exper
        output = []
        for partition in exper:
            if  isinstance(partition,list):
                output.append(compile(partition))

            elif partition == '+'or partition == '-':
                output[-2] = self.add_sub_cal(self,output[-2],output[-1],partition)
                output.pop(-1)

            elif partition == '*':
                output[-2] = self.mul_cal(self,output[-2],output[-1])
                output.pop(-1)

            else:
                output.append(partition)

        return output[0]

    def mul_cal(self,former,latter):
        class expr_compose:
            def __init__(expr):
                expr_devided = expr[0] + expr[1:].replace('+','/').replace('-','/-')#演算子ごとに'/'を付けるが先頭の'-'には'/'を付けない
                self.item_count = expr_devided.count('/')+1
                self.expr_compose = [Item]*self.item_count
                for ct,splited in enumerate(self.item_count):
                    self.expr_compose[ct] = Item(splited[ct])
        output= ''
        F_formura = expr_compose(former)
        L_formura = expr_compose(latter)
        for F_count in enumerate(F_formura.count):
            for L_count in enumerate(L_formura.count):
                number = F_formura.expr_compose[F_count].number * L_formura.expr_compose[L_count].number
                add_compose = ''
                if number == -1:
                    add_compose += str( '-' )
                elif number != 1:
                    add_compose += str( number )

                add_compose += ( F_formura.expr_compose[F_count] + L_formura.expr_compose[L_count] ).sorted()
                if add_compose == '-':   #文字が何もなくて定数が-1だった時への対処
                    add_compose = '-1'
                elif add_compose[0] != '-' and len(output) > 0:
                    add_compose = '+' + add_compose
                output += add_compose

        return self.cleaner(output)

    def add_sub_cal(self,former,latter,code):

        if latter[0] != '-':
            latter = '+' + latter

        if code == '+':
            output = former + latter

        else:
            output = former + latter.replace('+','/').replace('-','+').replace('/','-')

        return self.cleaner(output)

    def cleaner(expr):
        expr_devided = expr[0] + expr[1:].replace('+','/').replace('-','/-')#演算子ごとに'/'を付けるが先頭の'-'には'/'を付けない
        clean_list = [Item]
        for data in expr_devided.split('/'):
            current = Item(data)
            identical_compose = None
            for clean_list_partition in enumerate(clean_list):
                if clean_list_partition.alphabet_compose == current.alphabet_compose:
                    clean_list_partition.number += current.number
                    identical_compose = 'exited'
                    break
            if identical_compose == None:
                clean_list_partition.append(current)
        output = ''
        for clean_list_partition in clean_list:
            if clean_list_partition.number == 1:
                add_compose = clean_list_partition.alphabet_compose
            
            elif clean_list_partition.number == -1:
                add_compose = '-' + clean_list_partition.alphabet_compose

            elif clean_list_partition.number != 0:
                add_compose = str( clean_list_partition.number ) + clean_list_partition.alphabet_compose
            
            if add_compose == '-':   #文字が何もなくて定数が-1だった時への対処
                add_compose = '-1'

            elif add_compose[0] != '-' and len(output) > 0:
                add_compose = '+' + add_compose
            output += add_compose

        return output
        
data = input()
data = Method.convert_to_rpn(Method,data)
print(data)