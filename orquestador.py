# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:54:39 2021

@author: Moibe
"""

import simple

url = 'https://www.coding-depot.dev/paypalinfosample.xlsx'

#excel = simple.obtenExcel(url)

print("Aquí va a imprimir directamente la última celda...")
print(simple.celdaDiaria(simple.obtenExcel(url))) 

# resultado = simple.sumaValores(url, 9100, 9200, 'K')
# print(resultado)
