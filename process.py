from Calculation import mathod
from dataget import queue


syntax = input("式を入力してください")
syntax = syntax.replace(' ','')
syntax = syntax.replace('*', '')

value = mathod('test',syntax)
print(value.values)