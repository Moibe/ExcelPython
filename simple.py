# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:31:21 2021
Suma los totales entre dos rangos de celdas.

@author: Moibe
"""
import requests
import openpyxl
import filtrador 
import time


def obtenExcel(url, archivo):
      
        #Baja el excel indicado en la URL. 
        #Si la url tuviera un 0 significa que el archivo no baja, que está en local.
        if url is not 0 :
            
            r = requests.get(url, allow_redirects=True)
        
        #Ábrelo para trabajar con él.
        open(archivo, 'wb').write(r.content)

        
        print("Creando objetos de stream de Paypal.")
        #Crea los objetos con los que trabajarás el MoneyStream.
        libro_excel = openpyxl.load_workbook(archivo)
        hoja_excel = libro_excel.active
        
        return hoja_excel

def ultimaCelda(hoja_excel):
    
    ultima_celda = hoja_excel.max_row
    print(ultima_celda)
    #Ésta función puede definir la celda hasta el momento.
    #Pero también la última del día para usarse o nutrir un json.
    
    return ultima_celda


def sumaValores(**kwargs):
    
    filtro_producto = kwargs.get('filtro_producto', 'nada')
    print(filtro_producto)
    filtro_cuenta = kwargs.get('filtro_cuenta', 'nada')
    print(filtro_cuenta)
    celda_inicial = kwargs.get('celda_inicial', 'nada')
    celda_final = kwargs.get('celda_final', 'nada')
    hoja_excel = kwargs.get('hoja_excel', 'nada')
   
    total = 0
    iteraciones = 0
    print(total)
    print(iteraciones)
    
    for celda_inicial in range(celda_inicial, celda_final):
        
        iteraciones += 1
        print(iteraciones)
        fila_str = str(celda_inicial)
        
        celda_estado = 'G' + fila_str     
        celda_campaña = 'Q' + fila_str
        celda_cuenta = 'R' + fila_str 
        celda_usd = 'K' + fila_str   
        
       
        
        estado = hoja_excel[celda_estado].value
       
        
        valor_producto = hoja_excel[celda_campaña].value
       
        if valor_producto is None :
            valor_producto = "nada"
        
        valor_cuenta = hoja_excel[celda_cuenta].value
        
        if valor_cuenta is None :
            valor_producto = "nada"
        
        #Si no se agregó ninguno de los dos filtros, entonces no se usará el filtroTotal.
        if "nada" in filtro_producto and "nada" in filtro_cuenta:
            filtro = True
        else:
                       
            filtro = filtrador.filtroTotal(filtro_producto, filtro_cuenta, valor_producto, valor_cuenta) 
            print("ESTE ES EL RESULTADO DEL FILTRAJE...")
            print(filtro)
            
        if filtro is True: 
      
            try: 
                
                #Solo trabaja con las celdas cuyo estado es Completed.
                if(filtrador.filtroEstado(estado)) is True: 
                    
                    #Obten el valor original de la celda.
                    valor = hoja_excel[celda_usd].value
                    #Aquí estamos filtrando las excepciones, en éste caso 0 y neg.
                    #Si es 0 o negativo sumará 0. Si no, el valor real.
                    valor = filtrador.filtroNumeros(valor)
                   
                    total = total + valor
                    print("Si estamos SUMANDO, el total va en....")
                    print(total)
                        
                
            except: 
                        print("Error....")
                        
        else: 
            print ("El filtro fue false...")
                    
        
    
    resultado_final = total
    return resultado_final