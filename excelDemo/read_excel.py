import openpyxl
import datetime


def read_excel(file_name):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb["Student"]

    student_list = []

    for row in sheet.iter_rows(min_row=2, min_col=1):
        try:
            print(type(row))
            name = row[0].value
            percentage = float((row[1].value + row[2].value + row[3].value) / 3)
            percentage = round(percentage, 2)
            if percentage > 35:
                result = "Pass"
            else:
                result = "Fail"
            age = datetime.datetime.now().year - row[4].value.year
            student_list.append((name, percentage, result, age))
        except:
            print("Something bad happened")

    return student_list
