from lib3 import *
import sys

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

