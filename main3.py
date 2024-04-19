from lib3 import *
import sys
import pandas as pd
from lib3.classes import grafo

def main(nombre_archivo):
    archivo = nombre_archivo + ".xlsx" 
    
    #leer el archivos
    try:
        datos = pd.read_excel(archivo)
        print("Contenido del archivo:")
        print(datos)

        #obtener vértices y aristas
        vertices = set(datos['Origen']) | set(datos['Destino'])
        aristas = list(zip(datos['Origen'], datos['Destino'], datos['Peso']))

        #matriz
        print("\nMatriz de Adyacencia Ponderada:")
        matriz = pd.pivot_table(datos, values='Peso', index='Origen', columns='Destino', fill_value=0)
        print(matriz)

        #lista de relaciones
        grafo_test = grafo()
        for origen, destino, peso in aristas:
            grafo_test.addArista(origen, destino, peso)

        print("\nLista de Relaciones:")
        for arista in aristas:
            print(f"{arista[0]} -> {arista[1]}: Peso {arista[2]}")

        print("\nGrafo:")
        print(grafo_test)

        origen = 'B'
        destino = 'H'
        camino_mas_corto, peso_total = dijkstra(grafo_test, origen, destino)

        #camino más corto y su peso total
        print(f"\nCamino más corto desde {origen} hasta {destino}:")
        print(" -> ".join(camino_mas_corto))
        print(f"Peso total del camino: {peso_total}")

    except FileNotFoundError:
        print("El archivo especificado no se encontró.")

def dijkstra(grafo, origen, destino):
    #algoritmo de Dijkstra
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        nombre_archivo = input("¿Cuál es el nombre del archivo .xlsx?: ")
    else:
        nombre_archivo = sys.argv[1]
    main(nombre_archivo)


diccRel = {}

grafoTest = grafo()
grafoTest.addArista('A', 'B', 5)
grafoTest.addArista('A', 'C', 3)

grafoTest.addArista('B', 'A', 5)
grafoTest.addArista('B', 'C', 2)
grafoTest.addArista('B', 'D', 4)

grafoTest.addArista('C', 'A', 3)
grafoTest.addArista('C', 'B', 2)
grafoTest.addArista('C', 'D', 6)
grafoTest.addArista('C', 'E', 7)

grafoTest.addArista('D', 'B', 4)
grafoTest.addArista('D', 'C', 6)
grafoTest.addArista('D', 'E', 8)

grafoTest.addArista('E', 'C', 7)
grafoTest.addArista('E', 'D', 8)

origen = 'A'
destino = 'E'
path={}
visitados=[]

visitados.append( origen )
path[origen] = {'-':0}

llaves = grafoTest.aristas[origen].keys()
print(llaves)

for i in llaves:
    path[i]={origen: grafoTest.aristas[origen][i]}

print("primer iter:")
print(visitados)
print(path)

verticeAct = 'B'
visitados.append( verticeAct )
llaves = grafoTest.aristas[verticeAct].keys()
print(llaves)

for i in llaves:
    if i not in visitados:
        if i not in path: path[i]={}
        llave = list( path[verticeAct].keys() )
        acumulado = path[verticeAct][ llave[0] ]

        path[i].update({ verticeAct : grafoTest.aristas[verticeAct][i]+acumulado })

        #reviso si hay mas de 2 llaves en una llave del path
        if len(path[i]) == 2:
            kiss = list(path[i].keys())
            if kiss[0]>kiss[1]:
                del( path[i][ kiss[0] ])
            elif kiss[0]<kiss[1]:
                del( path[i][ kiss[1] ])
            pass

    #fin if not in visitados
# fin for i

print(path)
exit()

