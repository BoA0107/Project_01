# -*- coding:utf-8 -*-
from read_doc import *

filename = r'doc/home.xlsx'
ST_links = r'links'
ST_depoly = r'deploy_plan'
ST_level = r'level_info'
ST_others = r'others'

# links
links = read_doc(filename=filename, sheetname=ST_links)
links_dct = make_dct(links)

# deploy_plans
plan_info = read_doc(filename=filename, sheetname=ST_depoly, MaxLine=24)

# level
career_level = read_doc(filename=filename, sheetname=ST_level)

# others
others = read_line(filename=filename, sheetname=ST_others)
