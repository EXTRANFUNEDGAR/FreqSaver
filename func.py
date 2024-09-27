# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:00:19 2024

@author: EXTRANFUNEDGAR
"""
import json
from datetime import datetime

archivo = 'freq.json'
###########################
def agregar_freq(archivo_json, nuevo_dato):
    try:
        with open(archivo_json, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []
    
    
    datos.append(nuevo_dato)

   
    with open(archivo_json, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Datos agregados exitosamente.")
####################

def buscar_dato(archivo_json, clave, valor_buscado):
    try:
        
        with open(archivo_json, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe.")
        return
    
    
    resultados = [dato for dato in datos if dato.get(clave) == valor_buscado]

    if resultados:
        
        claves = resultados[0].keys()
        
        print("\nResultados encontrados:")
        print("-" * 40)  
        print(" | ".join(f"{clave: <15}" for clave in claves))  
        print("-" * 40)  
        
       
        for resultado in resultados:
            print(" | ".join(f"{str(valor): <15}" for valor in resultado.values()))  
        print("-" * 40)  
    else:
        print("No se encontraron resultados.")

###############################
def modulaciones():
        mod = input("\n1: AM\n2: FM\n3: PM\n4: FSK\n5: PAM\n6: QAM\n7: WFM\n8: PWM\n")
        
        if mod =="1":
            modu="AM"
        elif mod =="2":
            modu="FM"
        elif mod =="3":
            modu="PM"
        elif mod =="4":
            modu="AM"
        elif mod =="5":
            modu="PAM"
        elif mod =="6":
            modu="QAM"
        elif mod =="7":
            modu="WFM"
        elif mod =="8":
            modu="PWM"
        return modu
    
##########################################
def agregar():
        freq = input("Frecuencia: \n")
        print("Escoge la modulacion")
        modu = modulaciones()
        
        tag = input("\nTag:\n")
        des = input("Descripcion: \n")
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
        print(fecha)
        
        nuevo_dato = {
            "freq": freq,
            "modulation": modu,
            "tag":tag,
            "description":des,
            "hour":fecha
        }
        agregar_freq(archivo, nuevo_dato)


######################

def buscar():
            buscar = input("1: Frecuencia\n2: Modulacion\n3: Tag\n4: Descripcion\n5: Hora\n")
            if buscar =="1":
                busc="freq"
                val = input("Ingresa la frecuencia\n")
            elif buscar =="2":
                busc="modulation"
                print("Que modulacion quieres buscar\n")
                val = modulaciones()
            elif buscar =="3":
                busc="tag"
                val = input("Ingresa el tag\n")
            elif buscar =="4":
                busc="description"
                val = input("Ingresa la descripcion\n")
            elif buscar =="5":
                busc="hour"
                val = input("Ingresa la hora\n")
                
            buscar_dato(archivo, busc,val)