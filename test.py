import math
import numpy as np
def dataget():
    rowct=0
    columnct = 0
    queue = []
    while(1):
        row = input("対応する行列を入力してください")
        columnct = max(columnct,row.count(" ")+1)
        
        if row == "":
            break
        queue.append(row)
        rowct = rowct + 1
    cell = []*rowct*columnct
    for ct1 in range(rowct):
        cell[ct1] = [] * columnct
        ct2 = 0
        for values in queue[ct1].split(" "):
            cell[ct1][ct2] = values
            ct2 = ct2 + 1

#    for ct1 in range(rowct):
#        print(cell[ct1])
    return cell
    
def trip(syntax):
    ct = 0
    deep = 0
    length = len(syntax)
    for word in syntax :
        last = word
        if word == '(':
            deep = deep + 1

        elif word == ')':
            deep = deep - 1
            
        if deep == 0:
            if ct < length:
                return syntax
            else:
                return syntax[1:length-1]
        
        ct = ct + 1
    return syntax

# insert * inpomplete
def intergral(syntax):
    length = len(syntax)
    level = 0
    
    deepm = syntax.count("(")
    deepct = [0]*deepm

    ct = 0
    while ct < length:
        if syntax[ct] == '(':
            deep = deep + 1

        elif syntax[ct] == ')':
            deep = deep - 1
            deepct[deep] = deepct[deep] + 1
        else:
            if syntax[ct] != '+' & syntax[ct] != '-':
                deepct[deep] = deepct[deep] + 1
        if deepct[deep] >= 1:
            syntax = syntax[0:ct+1]+'*'+syntax[ct+1:length]
            length = length + 1
            deepct[deep] = 1
            ct = ct + 1
        ct = ct + 1
    return syntax

#   逆ポーランド記法への変換
def porandmake(syntax):
    if syntax == '':
        return ''
    syntax = trip(syntax)
    sign = 0
    deep = 0
    ct = 0
    length = len(syntax)
    if length == 1:
        return syntax
    #
    for Code in {'+','-','*'}:
        while(ct < length):
            if syntax[ct] == '(':
                deep = deep + 1

            elif syntax[ct] == ')':
                deep = deep - 1

            elif deep == 0:
                if syntax[ct] == Code:
                    code = Code
                    sign = 1
                    if code == '*':
                        former = syntax[0:ct]
                        latter = syntax[ct:length]
                    else:
                        former = syntax[0:ct]
                        latter = syntax[ct+1:length]
                    break
            ct = ct + 1
    #
    if sign == 1:
        former = porandmake(former)
        latter = porandmake(latter)
    else:
        return syntax

    if code == '*':
        return former+code+latter
    else:
        return former+latter+code
#   式の入力
def syntaxget():
    syntax = input("式を入力してください\n")
    syntax = syntax.replace(' ','')
    syntax = syntax.replace('*', '')
    syntax = porandmake(syntax)

    return syntax

syntax = syntaxget()
print(syntax)