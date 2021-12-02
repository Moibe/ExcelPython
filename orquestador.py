# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:54:39 2021

@author: Moibe
"""

import simple

url = 'https://www.coding-depot.dev/paypalinfosample.xlsx'

excel = simple.obtenExcel(url)

last_cell = simple.ultimaCelda(excel)
print("Ésta es la ZZELDA final....")
print(last_cell) 

resultado = simple.sumaValores(filtro_campaña = 'Digital Download ES', filtro_cuenta = 'Finland", url=url, celda_inicial = 9291, celda_final = last_cell, hoja_excel= excel)
print(resultado)
