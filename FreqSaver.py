# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:51:51 2024

@author: EXTRANFUNEDGAR
"""
from func import agregar,buscar

archivo = 'freq.json'

# Ejemplo de uso
if __name__ == "__main__":
    
    while True:
        print("Menu")
        op = input("\nEscoge una opcion \n1: Agregar Frecuencia \n2: Buscar \n3: Eliminar\n4: Salir\n")
        
        if op=="1":
            agregar()
       
        elif op =="2":
            print("Como quieres buscar?\n")
            buscar()
        elif op =="3":
            #eliminar():
            print("Se elimino el dato\n")
        elif op == "4":
            print("Saliendo del menu")
            break
        
    
    
    