import string
from calculation import Item,Method
from make_data import Input

def compile(exper):
    if 1 == 1:
        if len(exper) < 3:
            return exper

        # それぞれ普通の計算式が来たと仮定する
        stuck = []
        for partition in exper:
            if  isinstance(partition,list):
                stuck.append(compile(partition))

            elif partition == '+'or partition == '-':
                stuck[-2] = add_cal(stuck[-2],stuck[-1],partition)
                stuck.pop(-1)

            elif partition == '*':
                stuck[-2] = mul_cal(stuck[-2],stuck[-1])
                stuck.pop(-1)

            else:
                stuck.append(compile(partition))

    return stuck[0]

def mul_cal(former,latter):
    if 1 == 1:
        result= ''
        former = former[0] + former[1:].replace('+','/').replace('-','/-')
        latter = latter[0] + latter[1:].replace('+','/').replace('-','/-')
        for former_c in former.split('/'):
            if former_c[0] == '-':
                former_code = 'minus'
                former_c = former_c[1:]
            else:
                former_code = 'plus'

            for latter_c in latter.split('/'):
                if latter_c[0] == '-':
                    latter_code = 'minus'
                    latter_c = latter_c[1:]
                else:
                    latter_code = 'plus'

                if former_code == latter_code:
                    result += '+'
                else:
                    result += '-'

                if former_c[-1].isdigit() and ( latter_c[0].isdigit() or latter_c[:1].isdigit() ):
                    result += former_c + '|' + latter_c
                else:
                    result += former_c + latter_c

    return cleaner(result[1:])

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
    inventory = []
    for data in exper.split('/'):
        current = Item(data)
        identical = 0
        if len(inventory) > 0:
            for ct,comparison in enumerate(inventory):
                for ct_str in range(26):
                    if current.compose[ct_str] != comparison.compose[ct_str]:
                        break
                if ct_str == 25:
                    inventory[ct].number += current.number
                    identical = 1
                    break

        if identical == 0:
            inventory.append(current)

    result = ''
    for comparison in inventory:
        if comparison.number > 0 :
            result += '+'
            if comparison.number != 1:
                result += str(comparison.number)
        elif comparison.number != 0:
            result += '-'
            if comparison.number != -1:
                result += str( -1 * comparison.number)
        else:
            continue

        for ct_str in range(26):
            result += string.ascii_letters[ct_str]*comparison.compose[ct_str]

    if result[0] == '+':
        result = result[1:]

    return result

data = input()
data = Method.convert_to_rpn(Method,data)
print(data)
print(compile(data))