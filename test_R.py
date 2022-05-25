
        
print("対応する行列を入力してください")
values = []
while(1):
    # comes data from front
    row = input()
    if( row == ''):
        break
    values.append(row.split(" "))
for row in values:
    print(row)