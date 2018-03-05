numero_de_linhas  = 3
numero_de_colunas = 3
matriz = []
print('Digite os valores 1 ou 0 para Matriz 3 X 3 ')
for i in range(numero_de_linhas):
    linhas = []
    for j in range(numero_de_colunas):
        num = int(input('Digite o elemento {} X {} da Matriz: '.format(i,j)))
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


#Funcional
if matriz[0][0]==0 and matriz[0][1]== 0 and matriz[0][2]==0 or matriz[0][0] == 1 and  matriz[0][0] !=  matriz[0][1] and  matriz[0][0]!= matriz[0][2] or matriz[0][1] == 1 and  matriz[0][1] !=  matriz[0][0] and  matriz[0][1]!= matriz[0][2] or matriz[0][2] == 1 and  matriz[0][2] !=  matriz[0][0] and  matriz[0][2]!= matriz[0][1]:
    linha1 = (True)
else:
    linha1 =(False)
if  matriz[1][0]==0 and matriz[1][1] ==0 and matriz[1][2] ==0 or matriz[1][0] == 1 and  matriz[1][0] !=  matriz[1][1] and  matriz[1][0]!= matriz[1][2] or matriz[1][1] == 1 and  matriz[1][1] !=  matriz[1][0] and  matriz[1][1]!= matriz[1][2] or matriz[1][2] == 1 and  matriz[1][2] !=  matriz[1][0] and  matriz[1][2]!= matriz[1][1]:
    linha2 = (True)
else:
    linha2 =(False)
if matriz[2][0]==0 and matriz[2][1] ==0 and matriz[2][2] ==0 or matriz[2][0] == 1 and  matriz[2][0] !=  matriz[2][1] and  matriz[2][0]!= matriz[2][2] or matriz[2][0] == 1 and  matriz[2][1] !=  matriz[2][0] and  matriz[2][1]!= matriz[2][2] or matriz[2][2] == 1 and  matriz[2][2] !=  matriz[2][0] and  matriz[2][2]!= matriz[2][1]:
    linha3 = (True)
else:
    linha3 =(False)

if linha1 == (True) and linha2 == (True) and linha3 == (True):
    funcional = (True)
else:
    funcional = (False)
print('Funcional: {}'.format(funcional))
    
#Injetora
if matriz[0][0]==0 and matriz[1][0] == 0 and matriz[2][0] == 0 or matriz[0][0] == 1 and  matriz[0][0] !=  matriz[1][0] and  matriz[0][0]!= matriz[2][0] or matriz[1][0] == 1 and  matriz[1][0] !=  matriz[0][0] and  matriz[1][0]!= matriz[2][0] or matriz[2][0] == 1 and  matriz[2][0] !=  matriz[0][0] and  matriz[2][0]!= matriz[1][0]:
    coluna1 = (True) 
else:
    coluna1 =(False)
if matriz[0][1]==0 and matriz[1][1] == 0 and matriz[2][1] == 0 or matriz[0][1] == 1 and  matriz[0][1] !=  matriz[1][1] and  matriz[0][1]!= matriz[2][1] or matriz[1][1] == 1 and  matriz[1][1] !=  matriz[0][1] and  matriz[1][1]!= matriz[2][1] or matriz[2][1] == 1 and  matriz[2][1] !=  matriz[0][1] and  matriz[2][1]!= matriz[1][1]:
    coluna2 = (True)
else:
    coluna2 =(False)
if matriz[0][2]==0 and matriz[1][2] == 0 and matriz[2][0] == 0 or matriz[0][2] == 1 and  matriz[0][2] !=  matriz[1][2] and  matriz[2][0]!= matriz[2][2] or matriz[1][2] == 1 and  matriz[1][2] !=  matriz[0][2] and  matriz[1][2]!= matriz[2][2] or matriz[2][2] == 1 and  matriz[2][2] !=  matriz[0][2] and  matriz[2][2]!= matriz[1][2]:
    coluna3 = (True)
else:
    coluna3 =(False)

if coluna1 == (True) and coluna2 == (True) and coluna3 == (True):
    injetora = (True)
else:
    injetora = (False)
print('Injetora: {}'.format(injetora))

#Total

if matriz[0][0]==1 or matriz[0][1]==1 or matriz[0][2]==1:
    linha1 = (True)
else:
    linha1 = (False)
if matriz[1][0]==1 or matriz[1][1]==1 or matriz[1][2]==1:
    linha2 = (True)
else:
    linha2 = (False)
if matriz[2][0]==1 or matriz[2][1]==1 or matriz[2][2]==1:
    linha3 = (True)
else:
    linha3 = (False)

if linha1 == (True) and linha2 == (True) and linha3 == (True):
    total = (True)
else:
    total = (False)
print('Total: {}'.format(total))    


#Subrejetora

if matriz[0][0]==1 or matriz[1][0]==1 or matriz[2][0]==1:
    coluna1 = (True)
else:
    coluna1 = (False)
if matriz[0][1]==1 or matriz[1][1]==1 or matriz[2][1]==1:
    coluna2 = (True)
else:
    coluna2 = (False)
if matriz[0][2]==1 or matriz[1][2]==1 or matriz[2][2]==1:
    coluna3 = (True)
else:
    coluna3 = (False)

if coluna1 == (True) and coluna2 == (True) and coluna3 == (True):
    subrejetora = (True)
else:
    subrejetora = (False)
print('Subrejetora: {}'.format(subrejetora))

#Monomorfismo
if injetora == (True) and total == (True):
    monomorfismo = True
else:
    monomorfismo = False
print('Monomorfismo: {}'.format(monomorfismo))

#Epimorfismo
if funcional == (True) and subrejetora == (True):
    epimorfismo = True
else:
    epimorfismo = False
print('Epimorfismo: {}'.format(epimorfismo))

#Isomorfismo
print('Isomorfismo: ')
