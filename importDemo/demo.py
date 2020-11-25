row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))

multi_list = []

for row in range(row_num):
    multi_list.append([])
    for col in range(col_num):
        multi_list[row].append(row*col)

print(multi_list)