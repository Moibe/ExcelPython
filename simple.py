# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:31:21 2021
Suma los totales entre dos rangos de celdas.

@author: Moibe
"""
import requests
import openpyxl
import filtrador 

def obtenExcel(url):

        print("Descarga y revisión de datos de Paypal...")
        #Baja el excel indicado en la URL. 
        r = requests.get(url, allow_redirects=True)
        
        #Guardalo para trabajar con él.
        open('Paypal.xlsx', 'wb').write(r.content)

        
        print("Creando objetos de stream de Paypal.")
        #Crea los objetos con los que trabajarás el MoneyStream.
        libro_excel = openpyxl.load_workbook("Paypal.xlsx")
        hoja_excel = libro_excel.active
        
        return hoja_excel

def celdaDiaria(hoja_excel):
    
    ultima_celda = hoja_excel.max_row
    print(ultima_celda)
    #Ésta función puede definir la celda hasta el momento.
    #Pero también la última del día para usarse o nutrir un json.
    
    return ultima_celda


def sumaValores(url, celda_inicial, celda_final, columna, hoja_excel):
    
    total = 0
    
    for celda_inicial in range(celda_inicial, celda_final):
        
        fila_str = str(celda_inicial)
            
        celda_campaña = 'Q' + fila_str
        celda_cuenta = 'R' + fila_str 
        
        campaña = hoja_excel[celda_campaña].value
        cuenta = hoja_excel[celda_cuenta].value
        
        filtro = filtrador.filtroTotal(filtro_campaña = 'Digital Download ES', filtro_cuenta = 'DeepBlue', campaña = campaña, cuenta = cuenta) 
        
        if filtro is True: 
      
            try: 
                
                fila_str = str(celda_inicial)
                print("Fila: " + fila_str)
                celda_sumable = columna + fila_str
                valor = hoja_excel[celda_sumable].value
                #Aquí estamos filtrando las excepciones, en éste caso 0 y neg.
                valor = filtrador.filtroNumeros(valor)
                total = total + valor
                print(total)
                
            except: 
                        print("Error....")
                        
        else: 
            print ("El filtro fue false...")
                    
        
    
    resultado_final = total
    return resultado_final
                    
    # //Los negativos se deben ignorar.print
    # //Los ceros son los que debes debitar de su respectivo día, asumiendo q
    # regresas todos.
       
    