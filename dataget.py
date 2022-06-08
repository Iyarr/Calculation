from calculation import Method

class Input:
    def get_queue():
        queue = []
        print("の内容を入力してください\n")
        while(1):
            row = input()
            if( row == ''):
                break
            queue.append(row.split(" "))
        return queue

    def get_expr():
        return Method.convert_to_rpn(Method,input("式を入力してください\n").replace(' ',''))
