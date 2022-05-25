from calculation import Method

class Input:
    def dataget():
        values = []
        while(1):
            # comes data from front
            row = input()
            if( row == ''):
                break
            values.append(row.split(" "))
        return values

    def syntaxget():
        syntax = input("式を入力してください\n")
        syntax = syntax.replace(' ','')
        syntax = syntax.replace(' ','*')
        return Method.porandmake(Method,syntax)
