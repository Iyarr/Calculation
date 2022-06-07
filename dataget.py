from calculation import Method

class Input:
    def get_queue():
        queue = []
        print("の内容を入力してください\n")
        while(1):
            # comes data from front
            row = input()
            if( row == ''):
                break
            queue.append(row.split(" "))
        return queue

    def get_formula():
        formula = input("式を入力してください\n")
        formula = formula.replace(' ','')
        formula = formula.replace('*','')
        return Method.convert_formula_to_rpn(Method,formula)
