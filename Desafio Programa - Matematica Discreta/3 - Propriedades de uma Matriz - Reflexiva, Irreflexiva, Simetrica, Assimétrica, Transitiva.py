#Incerindo os dados na Matriz
numero_de_linhas  = int(input('Digite o número de linhas: '))
numero_de_colunas = int(input('Digite o número de colunas: '))
matriz = []
for i in range(numero_de_linhas):
    linhas = []
    for j in range(numero_de_colunas):
        num = int(input('Digite o elemento {} X {} : '.format(i,j)))
        linhas.append(num)
    matriz.append(linhas)

#Exibir Matriz
numero_de_linhas = len(matriz)
numero_de_colunas = len(matriz[0])
print('Sua matriz tem a caracteristica {} X {}.'.format(numero_de_linhas,numero_de_colunas))
for i in range(numero_de_linhas):
    for j in range(numero_de_colunas):
        #%3d define qual tamanho da distancia
        print("%3d" %(matriz[i][j]), end="")
    # pule uma linha
    print()
print(matriz[1][2])


#Reflexiva
#Ireflexiva
#Simetrica
#Anti-Simétrica ou Assimétrica
#Transitiva
