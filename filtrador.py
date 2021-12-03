# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:13:21 2021
Filtra valores, devuelve el valor o 0 si no cumplió los criterios.

@author: Moibe
"""

import time 

def filtroNumeros(valor):
    if (valor>0):
        print(valor)
        return valor
    else:
        valor = 0 
        print(valor)
        return valor

def filtroEstado(estado):
    if "Completed" in estado:
        
        print("Éste estado es True...")
        return True
    
def filtroTotal(texto_producto, texto_cuenta, value_producto, value_cuenta):
    
    if "nada" not in texto_producto:
        if texto_producto in value_producto:
           
            #Por lo tanto ahora debes buscar si está el segundo requisito...
            if "nada" not in texto_cuenta: 
                if texto_cuenta in value_cuenta:
                    #Los dos valores buscados si están en la fila, usa el valor.
                    return True
                else: 
                    #No encontró el segundo requisito, por eso será false.
                    print("El texto buscado NONONONONO está en la cuenta...")
                    time.sleep(3)
                    return False
            else: 
                #La segunda busqueda no se hizo, pero como si hubo la primera, cumple el requisito.
                print("El texto buscado NONONONONO está en la cuenta...")
                time.sleep(3)
                return True
        else: 
            #Si el texto no está en campaña, ya no tiene caso buscar en texto_cuenta, regresa false.
            print("El texto buscado NONONONONO está en la cuenta...")
            time.sleep(3)
            return False
            return False
    else:
        #Aquí llega si va vacio el texto campaña, aún así hay que evaluar texto_cuenta.
          if "nada" not in texto_cuenta: 
              if texto_cuenta in value_cuenta:
                  print("El texto_cuenta buscado si está en ésta celda...")#Los dos valores buscados si están en la fila, usa el valor.
                  return True
              else: 
                  #Si no encontró el texto no cumplió los dos requisitos regresa falso.
                  print("El texto buscado NONONONONO está en la cuenta...")
                  time.sleep(3)
                  return False
          else:
             #Aquí nunca debería llegar porque si los dos venían vacios la función no se debio ejecutar. 
             print("El texto buscado NONONONONO está en la cuenta...")
             time.sleep(3)
             return False
            
                
                
                
         
       
    
   
    
    
    
    
