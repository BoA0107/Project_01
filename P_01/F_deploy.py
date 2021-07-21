from read_doc import *

filename = r'doc/deploy.xlsx'

ST_answer = r'answer'
ST_branch = r'branch'


answer = read_doc(filename=filename,sheetname=ST_answer)
branch = read_doc(filename=filename,sheetname=ST_branch)