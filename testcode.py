from compile_test import cal

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

print("Please choose test item mul or add or clean")
data = input()
if data == "mul":
    test_item.test_mul()

elif data == "add":
    test_item.test_add_sub_cal()

elif data == "clean":
    test_item.test_cleaner()

 