import openpyxl.workbook
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment


def add_styles_to_workbook(wb):
    styleList = []

    headers = NamedStyle(name="headers")
    headers.font = Font(bold=True, size=20)
    bd = Side(style='thick', color="000000")
    headers.border = Border(left=bd, top=bd, right=bd, bottom=bd)
    headers.alignment = Alignment(horizontal="center")
    styleList.append(headers)

    cell = NamedStyle(name="cell")
    cell.font = Font(bold=False, size=14)
    cell_bd = Side(style='medium', color="000000")
    cell.border = Border(left=cell_bd, top=cell_bd, right=cell_bd, bottom=cell_bd)
    cell.alignment = Alignment(horizontal="center")
    styleList.append(cell)

    pass_cell = NamedStyle(name="pass_cell")
    pass_cell.font = Font(bold=False, size=14, color="77BB77")
    pass_cell.border = Border(left=cell_bd, top=cell_bd, right=cell_bd, bottom=cell_bd)
    pass_cell.alignment = Alignment(horizontal="center")
    styleList.append(pass_cell)

    fail_cell = NamedStyle(name="fail_cell")
    fail_cell.font = Font(bold=False, size=14, color="FF1111")
    fail_cell.border = Border(left=cell_bd, top=cell_bd, right=cell_bd, bottom=cell_bd)
    fail_cell.alignment = Alignment(horizontal="center")
    styleList.append(fail_cell)

    for style in styleList:
        if style.name not in wb.named_styles:
            wb.add_named_style(style)






