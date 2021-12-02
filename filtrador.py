# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:13:21 2021
Filtra valores, devuelve el valor o 0 si no cumplió los criterios.

@author: Moibe
"""

def filtroNumeros(valor):
    if (valor>0):
        print(valor)
        return valor
    else:
        valor = 0 
        print(valor)
        return valor

def filtroTotal(**kwargs):
    
    texto_campaña = kwargs.get('filtro_campaña', '')
    texto_cuenta = kwargs.get('filtro_cuenta', '')
    value_campaña = kwargs.get('value_campaña', '')
    value_cuenta = kwargs.get('value_cuenta', '')

    # if texto_cuenta in value_cuenta:
    #     print("El texto Finland si está en ésta celda...")
        
    #     return True
    
    if texto_campaña in value_campaña:
        print("El texto 'Digital Download ES' si está en ésta celda...")
        
        return True
    
    
