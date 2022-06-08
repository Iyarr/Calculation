from calculation import Method

#　キーボードからの入力
def get_expr():
    return convert_to_rpn(input("式を入力してください\n").replace(' ',''))

#   逆ポーランド記法への変換
def convert_to_rpn(expr):
    length = len(expr)
    if length < 2:
        return expr

    if find_brackets(expr) == length-1:
        expr = expr[1:-1]
    
    return find_add_sub(expr) or find_mul(expr) or expr

    #　不要な括弧の検出
def find_brackets(expr):
    deep = 0
    for ct, c in enumerate(expr):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -= 1

        if deep == 0:
            break

    return ct

    #　演算子の検出　＋、ー
def find_add_sub(expr):
    deep = 0
    for ct, c in enumerate(expr):
        if c == '(':
           deep += 1
        elif c == ')':
                deep += 1
        elif deep == 0:
            if c in '+-':
                return [convert_to_rpn(expr[:ct]),convert_to_rpn(expr[ct+1:]),c]
    return None

    #　演算子の検出　＊
def find_mul(expr):
    length = len(expr)
    level = 0
    deep = 0
    for ct, c in enumerate(expr):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -=  1

        if deep == 0:
            if c == '*':
                return [convert_to_rpn(expr[:ct]),convert_to_rpn(expr[ct+1:]),'*']
            if ct + 1 < length and c.isdigit():
                if expr[ct+1].isdigit() == False:
                    level += 1
                    if level == 1:
                        st = ct
            else :
                level += 1
                if level == 1:
                    st = ct
        if level == 2:
            return [convert_to_rpn(expr[:st+1]),convert_to_rpn(expr[st+1:]),'*']
    return None

expr = get_expr()
print(expr)