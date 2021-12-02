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

def filtroEstado(estado):
    if "Completed" in estado:
        
        print("Éste estado es True...")
        return True
    
def filtroTotal(**kwargs):
    
    texto_campaña = kwargs.get('filtro_campaña', 'nada')
    texto_cuenta = kwargs.get('filtro_cuenta', 'nada')
    value_campaña = kwargs.get('value_campaña', '')
    value_cuenta = kwargs.get('value_cuenta', '')
    
    print("Texto campaña")
    print(texto_campaña)
    print("Texto cuenta")
    print(texto_cuenta)
     
    if "nada" not in texto_campaña:
        if texto_campaña in value_campaña:
            print("El texto buscado si está en ésta celda...")
            #Por lo tanto ahora debes buscar si está el segundo requisito...
            if "nada" not in texto_cuenta: 
                if texto_cuenta in value_cuenta:
                    print("El texto buscado si está en ésta celda...")
                    #Los dos valores buscados si están en la fila, usa el valor.
                    return True
                else: 
                    #No encontró el segundo requisito, por eso será false.
                    return False
            else: 
                #La segunda busqueda no se hizo, pero como si hubo la primera, cumple el requisito.
                return True
        else: 
            #Si el texto no está en campaña, ya no tiene caso buscar en texto_cuenta, regresa false.
            return False
    else:
        #Aquí llega si va vacio el texto campaña, aún así hay que evaluar texto_cuenta.
          if "nada" not in texto_cuenta: 
              if texto_cuenta in value_cuenta:
                  print("El texto_cuenta buscado si está en ésta celda...")#Los dos valores buscados si están en la fila, usa el valor.
                  return True
              else: 
                  #Si no encontró el texto no cumplió los dos requisitos regresa falso.
                  return False
          else:
             #Aquí nunca debería llegar porque si los dos venían vacios la función no se debio ejecutar. 
             return False
            
                
                
                
         
       
    
   
    
    
    
    
