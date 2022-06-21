import numpy
from calculation import Method
from make_data import Input
from make_data import Queue

def intensive():
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
            stuck[-2] = Method.calculator(former,latter,dic)
            stuck = stuck[:-2]
                
    print(stuck)

intensive()
