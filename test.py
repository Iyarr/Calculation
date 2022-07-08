import string
from calculation import Item,Method
from make_data import Input

def compile(exper):
    if 1 == 1:
        if len(exper) < 3:
            return exper
        elif exper[2] in '-+*' == False:
            return exper

        # それぞれ普通の計算式が来たと仮定する
        stuck = []
        for partition in exper:
            if partition in '-+':
                stuck[-2] = add_cal(compile(stuck[-2]),compile(stuck[-1]),partition)
                stuck.pop(-1)

            elif partition == '*':
                stuck[-2] = mul_cal(compile(stuck[-2]),compile(stuck[-1]))
                stuck.pop(-1)

            else:
                stuck.append(partition)

    return stuck[0]

def mul_cal(former,latter):
    if 1 == 1:
        result= []
        for former_c in former.split('/'):
            for latter_c in latter.split('/'):
                if former_c[-1].isdigit() and ( latter_c[0].isdigit() or latter_c[:1].isdigit() ):
                    result += former_c + '|' + latter_c
                else:
                    result += former_c + latter_c

    return cleaner(result)

def add_cal(former,latter,code):

    if latter[0] != '-':
        latter = '+' + latter

    if code == '+':
        result = former + latter

    else:
        result = former + latter.replace('+','/').replace('-','+').replace('/','-')

    return cleaner(result)

def cleaner(exper):
    exper = exper[0] + exper[1:].replace('+','/').replace('-','/-')
    inventory = [Item]
    for data in exper.split('/'):
        current = Item(data)
        identical = 1
        if len(inventory) > 0:
            for comparison in inventory:
                for ct_str in range(52):
                    if current.compose[ct_str] != comparison.compose[ct_str]:
                        identical = 0
                        break
                if identical == 1:
                    comparison.number += current.number
                    break
        else:
            identical = 0
    
        if identical == 0:
            inventory.append(current)
    result = ''
    for comparison in inventory:
        if comparison.number > 0:
            result += '+' + str(comparison.number)
        elif comparison.number == 0:
            continue

        for ct_str in range(52):
            result += string.ascii_letters[ct_str]*comparison.compose[ct_str]

    if result[0] == '+':
        result = result[1:]

    return result

data = input()
data = Method.convert_to_rpn(Method,data)
print(data)
print(compile(data))