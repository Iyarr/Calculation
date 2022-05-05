import math
import numpy as np
def dataget():
    rowct=0
    columnct = 0
    queue = []
    while(1):
        row = input("対応する行列を入力してください")
        columnct = max(columnct,row.count(" ")+1)
        
        if( row == ""):
            break
        queue.append(row)
        rowct = rowct + 1
    cell = ["NULL"]*rowct*columnct
    for ct1 in range(rowct):
        cell[ct1] = ["NULL"] * columnct
        ct2 = 0
        for values in queue[ct1].split(" "):
            cell[ct1][ct2] = values
            ct2 = ct2 + 1

#    for ct1 in range(rowct):
#        print(cell[ct1])
    return cell
def separate(syntax):
    len = syntax.strlen()
    entity = []*3
    sign = 0
    ct = 0
    while(ct < len):
        if syntax[ct] == '(':
            deep = deep + 1

        elif syntax[ct] == ')':
            deep = deep - 1

        elif syntax[ct] == '+':
            syntax[ct] = ' '
            if( deep == 0 ):
                entity[0] = '+'
                entity[1] = syntax.split(' ',0)
                entity[2] = syntax.split(' ',1)
        elif syntax[ct] == '-':
            syntax[ct] = ' '
            if( deep == 0 ):
                entity[0] = '-'
                entity[1] = syntax.split(' ',0)
                entity[2] = syntax.split(' ',1)

    return entity
def divideword(syntax):
    len = syntax.strlen()



    return syntax

#   逆ポーランド記法への変換
def porandmake(syntax):
    deep = 0
    ct = 0
    len = syntax.strlen()
    entity = separate(syntax)
    tree = []*3

    tree[0] = entity[0]

    tree[1] = porandmake(entity[1])
    tree[2] = porandmake(entity[2])
    

    return syntax
#   式の入力
def syntaxget():
    syntax = input("式を入力してください")
    syntax = syntax.replace(' ','')
    syntax = syntax.replace('*', '')
    len = syntax.strlen()
    syntax = porandmake(syntax,len)

    return syntax

syntax = syntaxget()
data = dataget()
