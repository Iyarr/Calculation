import math
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
#   逆ポーランド記法への変換
def porandmake(syntax):
    ct1 = 1
    ct2 = 1
    

    return syntax
#   式の入力
def syntaxget():
    syntax = input("式を入力してください")
    syntax.strip()
    syntax = porandmake(syntax)
    return syntax

syntax = syntaxget()
data = dataget()
