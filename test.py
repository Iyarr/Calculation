import string
from calculation import Item
from make_data import Input

def compile(exper):
    if 1 == 1:
        if len(exper) < 3:
            return exper
        elif exper[2] in '-+*' == False:
            return exper
        
        # それぞれ普通の計算式が来たと仮定する
        former = compile(exper[0]).replace('+','/').replace('-','/-')
        latter = compile(exper[1]).replace('+','/').replace('-','/-')
        code = exper[2]
        result = ''

        if code in '+-':
            sign = 0
            for former_c in former.split('/'):
                if former_c.isdigit() == True:
                    sign = 1
                    break
            
            if sign == 1:
                for latter_c in latter.split('/'):
                    if latter_c.isdigit() == True:
                        if code == '+':
                            num = int(former_c)+int(latter_c)
                        else:
                            num = int(former_c)-int(latter_c)
                        
                        former = former +'/'+ str(num)
                        former = former.replace(former_c,'').replace('//','/')
                        latter = latter.replace(latter_c,'').replace('//','/')
                        break

            former = former.replace('/-','-').replace('/','+').strip('+')
            latter = latter.replace('/-','-').replace('/','+').strip('+')

            if latter == '':
                return former

            elif latter[0] != '-':
                latter = '+' + latter

            if code == '+':
                result = former+latter
            else:
                result = former+latter.replace('+','/').replace('-','+').replace('/','-')
            
        elif code == '*':
            for former_pertition in former.split('*'):
                for latter_pertition in latter.split('*'):
                    result = result + mul_cal(former_pertition,latter_pertition)

    return result

def mul_cal(former,latter):
    if 1 == 1:
        former_item = Item(former)
        latter_item = Item(latter)
        result = str(former_item.number * latter_item.number)
        if result == '1':
            result = ''
        for ct_str in range(52):
            former_item.compose[ct_str] += latter_item.compose[ct_str]
            for log in range(former_item.compose[ct_str]):
                result = result + string.ascii_letters[ct_str]
    return result

data = Input.get_expr()
print(data)