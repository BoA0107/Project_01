from read_doc import *

filename = r'doc/SQL.xlsx'
ST_Batch = r'Batch'
ST_Deploy = r'Deploy'
ST_ShouDao =r'ShouDao'
ST_Other = r'other'
Batch = read_dict(filename, sheetname=ST_Batch)
deploy = read_dict(filename, sheetname=ST_Deploy)
ShouDao = read_dict(filename, sheetname=ST_ShouDao)
other = read_dict(filename, sheetname=ST_Other)