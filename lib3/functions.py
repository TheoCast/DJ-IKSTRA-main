
def printDicc(dicc):
    for i in dicc:
        print(f'Vertice: {i}')
        for j in dicc[i]:
            print(f'\tRel: {j}, peso: {dicc[i][j]}')
    return ''
    