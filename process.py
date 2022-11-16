from calculation import Method
from make_data import Input,Queue

def index():
    expr = Input.get_expr()
    array = Method.convert_to_str(Method,expr)
    q_stuck = []
    stuck = []
    mark = []
    #　使用されている文字を記録
    for dic in array:
        if mark.count(dic) == 0:
            #　まだ入っていない文字を格納
            mark.append(dic)
            #　文字に対応する行列を登録
            q_stuck.append(Queue(dic))

    for dic in expr:
        if dic.isalpha() == True or dic.isdigit() == True:
            for desc in q_stuck:
                if dic == desc.name:
                    stuck.append(desc.entity)
                    break
            
        else:
            former = stuck[-2]
            latter = stuck[-1]
            if former.isdigit() == True:
                if latter.isdigit() == True:
                    if dic == '+':
                        stuck[-2] = str(int(former)+int(latter))
                    if dic == '-':
                        stuck[-2] = str(int(former)-int(latter))
                    else:
                        stuck[-2] = str(int(former)*int(latter))
                else:
                    stuck[-2] = Method.realnum_mixed_calculator(latter,former,dic)
            else:
                if latter.isdigit() == True:
                    stuck[-2] = Method.realnum_mixed_calculator(former,latter,dic)
                else:
                    stuck[-2] = Method.calculator(former,latter,dic)

            stuck.pop(-1)

    print(stuck)

index()
