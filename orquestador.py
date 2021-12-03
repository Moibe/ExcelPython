# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:54:39 2021

@author: Moibe
"""

import simple

url = 'https://www.coding-depot.dev/paypalinfosample.xlsx'

excel = simple.obtenExcel(url)

last_cell = simple.ultimaCelda(excel)

#Usar éstas variables.
#filtro_cuenta = 'MMC'
#filtro_producto = "EN"
resultado = simple.sumaValores(celda_inicial = 9291, celda_final = last_cell, hoja_excel= excel)
print(resultado)
