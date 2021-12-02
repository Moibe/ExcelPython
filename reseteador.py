# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 03:47:54 2021

@author: Moibe
El Reseteador debe de correr a las 00:00 de cada día para poner todos los valores del Json en ceros.
Previo a eso debe de guardar la última versión del Json como un archivo fechado. 
"""
import json 
import time 
import openpyxl
import requests

#Obtención de la última celda del día de Paypal: 

print("Descarga y revisión de datos de Paypal...")
#Baja una actualización del archivo de ventas. 
url = 'https://www.coding-depot.dev/paypalinfosample.xlsx'
r = requests.get(url, allow_redirects=True)

open('MoneyStream.xlsx', 'wb').write(r.content)

print("Creando objetos de stream de Paypal.")
#Crea los objetos con los que trabajarás el MoneyStream.
wb_moneystream = openpyxl.load_workbook("MoneyStream.xlsx")
ws_moneystream = wb_moneystream.active


#Como el reseteador se correrá a las 00:00 se asume entonces que la max row representa a la última venta del día.
ultima_venta_dia = ws_moneystream.max_row
print("Última venta del día:")
time.sleep(2)
print(ultima_venta_dia)
time.sleep(11)


#Descarga y muestra los valores actuales de JsParam: 
print("Descarga de Json con los valores actuales. ") 


try:
    with open('rango.json') as fp:
        js_param = json.load(fp)
    
except IndexError as e:
    time.sleep(1)
    print("Llegamos a un except.")
    print(e)
    
#Obtener los valores que teníamos guardados de la última revisión. 
for row in js_param: 
    
    #Valores generales:
    all_last_time = row['all_last_time']
    ads_last_cell = row['adstotals_last_cell']
    ads_spent = row['ads_spent']
    paypal_daily_last_cell = row['paypal_daily_last_cell']
    #Valores de los productos:
    valor_en = row['paypal_en']
    valor_es = row['paypal_es']
    valor_pt = row['paypal_pt']
    valor_uk = row['paypal_uk']
    valor_fr = row['paypal_fr']
    valor_de = row['paypal_de']
    valor_eu = row['paypal_eu']
    #Valores de las cuentas: 
    valor_alpha = row['paypal_alpha']
    valor_fuel = row['paypal_fuel']
    valor_gold = row['paypal_gold']
    valor_grande = row['paypal_grande']
    valor_gsm = row['paypal_gsm']
    valor_joy = row['paypal_joy']
    valor_linked = row['paypal_linked']
    valor_telsat = row['paypal_telsat'] 
       
    paypal_total = row['paypal_total']
    all_win = row['all_win']

print("Variables obtenidas:")  
print("all_last_time:")
print(all_last_time) 
print("ads_last_cell:")
print(ads_last_cell) 
print("ads_spent:")
print(ads_spent) 
print("paypal_daily_last_cell:")
print(paypal_daily_last_cell) 
print("paypal_today:")
print(paypal_total) 
print("all_win:")
print(all_win) 
time.sleep(1)
print("EN:")
print(valor_en)
print("ES:")
print(valor_es)
print("PT:")
print(valor_pt)
print("UK:")
print(valor_uk)
print("FR:")
print(valor_fr)
print("DE:")
print(valor_de)
print("EU:")
print(valor_eu)
time.sleep(5)
print("Alpha:")
print(valor_alpha)
print("Fuel:")
print(valor_fuel)
print("Gold:")
print(valor_gold)
print("Grande Gold:")
print(valor_grande)
print("GSM:")
print(valor_gsm)
print("Joy:")
print(valor_joy)
print("LinkedSys:")
print(valor_linked)
print("Telsat:")
print(valor_telsat)
time.sleep(1)

print("Listo para resetear: ")
time.sleep(1)

for row in js_param:
    
    print("Estos serán los nuevos valores a guardar: ")
    #row['all_last_time'] = timeTag
    
    row['all_win'] = 0
    row['ads_last_cell'] = 1
    row['adscampaigns_last_cell'] = 1
    row['adstotals_last_cell'] = 1
    row['adscampaigns_last_cell'] = 2 
    
    #Solo para pruebas antes de automatizar a 00:00
    #Aquí debes de poner el valor de la última celda del día anterior. 
    row['paypal_daily_last_cell'] = 7474
    
    
    #Éste es el correcto para producción.
    #row['paypal_daily_last_cell'] = ultima_venta_dia 
    
    row['paypal_total'] = 0
    
    #Valores Generales
    row['ads_spent'] = 0
    
# =============================================================================
#     #Valores de campañas:
#     row['gp_aleman'] = 0
#     row['gp_portugues'] = 0
#     row['actual_reinoUnido'] = 0
#     row['gp_english'] = 0
#     row['gp_europe'] = 0
#     row['gp_espanol'] = 0
#     row['actual_frances'] = 0
#     row['gp_englishWorld'] = 0
# =============================================================================
    
    #Valores por producto:
    row['paypal_en'] = 0
    row['paypal_es'] = 0
    row['paypal_pt'] = 0
    row['paypal_uk'] = 0
    row['paypal_fr'] = 0
    row['paypal_de'] = 0
    row['paypal_eu'] = 0
    row['paypal_us'] = 0
    #Valores por cuenta: 
    row['paypal_alpha'] = 0
    row['paypal_fuel'] = 0
    row['paypal_gold'] = 0
    row['paypal_nuevoOro'] = 0
    row['paypal_gsm'] = 0
    row['paypal_joy'] = 0
    row['paypal_linked'] = 0
    row['paypal_telsat'] = 0
    row['paypal_next'] = 0 
    row['paypal_tomahawk'] = 0

    
    print("Y así queda nuestro nuevo set:")
    print(js_param)
        
    #Escribe 
    try: 
        print("Ya va a escribir el nuevo json......")
        time.sleep(1)
        with open('rango.json', 'w', encoding='utf-8') as jsonf: 
            jsonf.write(json.dumps(js_param, indent=0)) 
            print("Ya imprimió.")
    except IndexError as e:
           time.sleep(1)
           print("Llegamos a un except.")
           print(e)
