import read_excel
import openpyxl
import applyStyleToExcel


def write_excel(result, file_path):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(("Name", "Percentage", "Result", "Age"))
    for i in result:
        sheet.append(i)

    wb.save(file_path)
    applyStyleToExcel.apply_styles_to_excel(file_path)
