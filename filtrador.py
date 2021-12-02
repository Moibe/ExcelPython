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
    
    filtro_campaña = kwargs.get('filtro_campaña', '')
    filtro_cuenta = kwargs.get('filtro_cuenta', '')
    campaña = kwargs.get('campaña', '')
    cuenta = kwargs.get('cuenta', '')

    if cuenta in celda_cuenta:
        print("El texto si está en ésta celda...")
        
        return True
    
    
