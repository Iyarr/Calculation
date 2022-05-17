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

def separate(syntax):
    length = len(syntax)
    deep = 0
    ct = 0
    while(ct < length):
        if syntax[ct] == '(':
            deep = deep + 1

        elif syntax[ct] == ')':
            deep = deep - 1

        elif deep == 0:
            if syntax[ct] == '+':
                syntax[ct] = ' '
                return np.array('+',syntax[0:ct-1],syntax[ct+1:length])
            elif syntax[ct] == '-':
                syntax[ct] = ' '
                return np.array('-',syntax[0:ct-1],syntax[ct+1:length])
        ct = ct + 1

    return intergral(syntax)
    
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
                return syntax[1:length-2]
        
        ct = ct + 1

    return syntax

# insert *
def intergral(syntax):
    ct = 0
    for word in syntax:
        if word == '(':
            deep = deep + 1

        elif word == ')':
            deep = deep - 1
            ct = ct + 1
        else:
            if deep == 0:
                ct = ct + 1

    return syntax

#   逆ポーランド記法への変換
def porandmake(syntax):
    syntax = trip(syntax)
    deep = 0
    ct = 0
    length = len(syntax)
    entity = separate(syntax)
    tree = []*3

    tree[0] = entity[0]

    tree[1] = porandmake(entity[1])
    tree[2] = porandmake(entity[2])

    syntax = tree[1]+tree[2]+tree[0]

    return syntax
#   式の入力
def syntaxget():
    syntax = input("式を入力してください\n")
    syntax = syntax.replace(' ','')
    syntax = syntax.replace('*', '')
    syntax = porandmake(list(syntax))

    return syntax

syntax = syntaxget()