# -*- coding:utf-8 -*-
from openpyxl import *


# read excel


def read_doc(filename, sheetname, MaxLine=0):
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name(sheetname)
    x = sheet.max_column
    y = sheet.max_row

    content = []
    for x in range(1, x + 1):
        c = []


def read_dict(filename, sheetname):
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name(sheetname)
    x = sheet.max_row
    dct = {}
    for i in range(1, x + 1):
        content = sheet.cell(i, 1).value
        if content != None:
            key = content
            dct[key]=[]
            val = sheet.cell(i,2).value
            dct[key].append(val)
        else:
            val = sheet.cell(i, 2).value
            dct[key].append(val)
    return dct
