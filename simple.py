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

def ultimaCelda(hoja_excel):
    
    ultima_celda = hoja_excel.max_row
    print(ultima_celda)
    #Ésta función puede definir la celda hasta el momento.
    #Pero también la última del día para usarse o nutrir un json.
    
    return ultima_celda


def sumaValores(**kwargs):
    
    filtro_campaña = kwargs.get('filtro_campaña', 'nada')
    print("Este es el filtro de la campaña-campaña...")
    print(filtro_campaña)
    filtro_cuenta = kwargs.get('filtro_cuenta', 'nada')
    print("Este es el filtro de la cuenta-cuenta...")
    print(filtro_cuenta)
    url = kwargs.get('url', 'nada')
    celda_inicial = kwargs.get('celda_inicial', 'nada')
    celda_final = kwargs.get('celda_final', 'nada')
    hoja_excel = kwargs.get('hoja_excel', 'nada')
    
    
    url, celda_inicial, celda_final, hoja_excel
    total = 0
    
    for celda_inicial in range(celda_inicial, celda_final):
        
        fila_str = str(celda_inicial)
        
        celda_estado = 'G' + fila_str     
        celda_campaña = 'Q' + fila_str
        celda_cuenta = 'R' + fila_str 
        celda_usd = 'K' + fila_str   
        
        estado = hoja_excel[celda_estado].value
        print(estado)
        campaña = hoja_excel[celda_campaña].value
        cuenta = hoja_excel[celda_cuenta].value
        
        #Si no se agregó ninguno de los dos filtros, entonces no se usará el filtroTotal.
        if "nada" in filtro_campaña and "nada" in filtro_cuenta:
            filtro = True
        else:
            filtro = filtrador.filtroTotal(texto_campaña = filtro_campaña, texto_cuenta = filtro_cuenta, value_campaña = campaña, value_cuenta = cuenta) 
        
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
                        
                
            except: 
                        print("Error....")
                        
        else: 
            print ("El filtro fue false...")
                    
        
    
    resultado_final = total
    return resultado_final
                    
    # //Los negativos se deben ignorar.print
    # //Los ceros son los que debes debitar de su respectivo día, asumiendo q
    # regresas todos.
       
    