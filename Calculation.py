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
def porandmake(syntax,ct):
    deep = 0
    st = ct
    while( syntax[ct] == ')' and deep == 0 ):
        if ct >= syntax.strlen():
            break

        if syntax[ct] == '(':
            deep = deep + 1

        elif syntax[ct] == ')':
            deep = deep - 1

        elif syntax[ct] == '+':
            if( deep == 0 ):
                calculate = ct
        
        ct = ct+1
    

    return syntax
#   式の入力
def syntaxget():
    syntax = input("式を入力してください")
    syntax = syntax.replace(' ','')
    syntax = syntax.replace('*', '')
    mount = syntax.count('(')
    ctmax = syntax.strlen()
    deep = 0
    while( 0 < mount ):
        ct = 0
        while( ct < ctmax ):
            if syntax[ct] == '(':
                deep = deep + 1

            elif syntax[ct] == ')':
                deep = deep - 1
            
            else:
                if( mount == deep ):
                    syntax = porandmake(syntax,ct)

        mount = mount - 1


        
    syntax = porandmake(syntax)
    syntax = syntax.replace('(', '')
    syntax = syntax.replace(')', '')
    return syntax

syntax = syntaxget()
data = dataget()
