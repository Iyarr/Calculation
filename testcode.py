from compile_test import Item,cal
from rpm_test import Method

class test_item:
    def test_mul():
        former = input()
        latter = input()
        calculated = cal.mul_cal(cal,former,latter)
        print(calculated)

    def test_add_sub_cal():
        former = input()
        latter = input()
        code = input()
        calculated = cal.add_sub_cal(cal,former,latter,code)
        print(calculated)

    def test_cleaner():
        expr = input()
        cleaned = cal.cleaner(expr)
        print(cleaned)

    def test_entire():
        rpm = Method.convert_to_rpn(Method,input())
        print(rpm)
        compile = cal.compile(cal,rpm)
        print(compile)

print("Please choose test item mul or add or clean")
data = input()
if data == "m":
    test_item.test_mul()

elif data == "a":
    test_item.test_add_sub_cal()

elif data == "c":
    test_item.test_cleaner()

elif data == "e":
    test_item.test_entire()