# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:51:51 2024

@author: EXTRANFUNEDGAR
"""
import json
###########################
# Función para agregar datos a un archivo JSON
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
# Función para buscar datos en un archivo JSON
def buscar_dato(archivo_json, clave, valor_buscado):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe.")
        return
    
    # Buscar datos que coincidan con la clave y el valor
    resultados = [dato for dato in datos if dato.get(clave) == valor_buscado]

    # Imprimir los resultados de la búsqueda
    if resultados:
        print("Resultados encontrados:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron resultados.")

# Ejemplo de uso
if __name__ == "__main__":
    archivo = 'freq.json'

    # Agregar un nuevo dato (puedes cambiar esto por cualquier otra información que quieras)
    nuevo_dato = {"freq": "590.000", "modulation": "AM","tag":"","description":"prueba","hour":"20:29"}
    agregar_freq(archivo, nuevo_dato)

    # Buscar un dato
    buscar_dato(archivo, "modulation", "AM")