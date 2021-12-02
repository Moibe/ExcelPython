# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:02:08 2021

@author: Moibe
"""


import requests


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSCgnrjgdwlXI_5FxEvNxhzfDiMKFgFH2ryQ4X4xxAg1Zh-OSD4w10dfAMqDoy7grRr_UhEIxGo9zx4/pub?output=xlsx'
r = requests.get(url, allow_redirects=True)

open('publicstream.xlsx', 'wb').write(r.content)