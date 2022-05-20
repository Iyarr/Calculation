
    #   逆ポーランド記法への変換
def porandmake(syntax):
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
                former = porandmake(syntax[0:ct])
                latter = porandmake(syntax[ct+1:length])
                sign = 1
                return former+latter+syntax[ct]
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
                    
            elif deep == 0:
                level = level + 1
                if level == 1:
                    st = ct

            if level == 2:
                former = porandmake(syntax[0:st+1])
                latter = porandmake(syntax[st+1:length])
                return former+latter+'*'
            ct = ct + 1

    return syntax
#   式の入力
def syntaxget():
    syntax = input("式を入力してください\n")
    syntax = syntax.replace(' ','')
    syntax = syntax.replace(' ','*')
    syntax = porandmake(syntax)
    return syntax

syntax = syntaxget()
print(syntax)
