import read_excel, write_excel

result = read_excel.read_excel("Students.xlsx")
write_excel.write_excel(result, "StudentResult.xlsx")
