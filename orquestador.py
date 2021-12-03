# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:54:39 2021
Desde aquí lanzo las operaciones para los reportes.
@author: Moibe
"""

import simple

#Dataset de Catálogo
url = 0
catalogo = 'Cuentas-Productos.xlsx'

#Dataset para Paypal. 
url_paypal = 'https://www.coding-depot.dev/paypalinfosample.xlsx'
archivo_paypal = 'Paypal.xlsx'


#Obtén catálogo de cuentas y productos. 
excel_catalogo = simple.obtenExcel(url, catalogo)

#Obtén excel de Paypal.
excel_paypal = simple.obtenExcel(url, archivo_paypal)
last_cell = simple.ultimaCelda(excel_paypal)

#Usar éstas variables.
#filtro_cuenta = 'MMC'
#filtro_producto = "EN"
resultado = simple.sumaValores(celda_inicial = 9291, celda_final = last_cell, hoja_excel= excel_paypal)
print(resultado)
