﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos por categoria y pais ")
    print("3- Video tendencia por pais")
    print("4- Video tendencia por categoria")
    print ("5- Video por mas likes")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initcatalog()
        controller.cargardatos(catalog)
        print("Se cargo la informacion del catalogo")
        print("se cargaron:" +str(lt.size(catalog["videos"]))+ "videos")

    elif int(inputs[0]) == 2:
        t1 = time.process_time()
        print("Se ejecuto requerimiento 1 ")
        t2 = time.process_time()
        print(t2-t1)
    
    elif int(inputs[0]) == 3:
        print("Se ejecuto requerimiento 2 ")
    
    elif int(inputs[0]) == 4:
        print("Se ejecuto requerimiento 3 ")
    
    elif int(inputs[0]) == 5:
        print("Se ejecuto requerimiento 4 ")

    else:
        sys.exit(0)
sys.exit(0)