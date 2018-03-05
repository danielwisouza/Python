def obrigado():
    volta = input('Deseja voltar ao menu? S ou N: ')
    if volta == 'S' or volta == 'S':
        menu()
    else:
        print('OBRIGADO POR USAR O EASY DISCRETE MATHEMATICS !! ')
         
def resposta():
    global resp
    resp = int(input('Responda qual operação deseja fazer: '))
    escopo()
    return resp

def menu():
    print('|------------------------------------------------------------------------------|')
    print('|                         EASY DISCRETE MATHEMATICS                            |')
    print('|          Daniel Willians Ignacio de Souza - 1º Semestre Banco de Dados       |')
    print('|                 Professor: Marcos Allan Ferreira Goncalves                   |')
    print('|------------------------------------------------------------------------------|')
    print('| 1 - Relações de Conjunto                                                     |')
    print('| 2 - Olhando as Matrizes -  Funcional, Injetora, Total, Subjetora             |')
    print('| 3 - Matrizes - Reflexiva, Irreflexiva, Simetrica, Anti-simétrica.            |')
    print('|------------------------------------------------------------------------------|')

    resposta()
    
def escopo():
    if resp == 1:
        print('| 1 - Relações de Conjunto                                                     |')
        conjunto1 = []
        conjunto2 = []
        i = 0

        x = int(input('Quantos elementos tem o conjunto A: '))
        while i < x:
            conj1 = int(input('Digite o {}º termo do congunto A: '.format(i)))
            conjunto1.append(conj1)
            i = i + 1
        i = 0

        y = int(input('Quantos elementos tem o conjunto B: '))
        while i < y:
            conj2 = int(input('Digite o {}º termo do congunto A '.format(i)))
            conjunto2.append(conj2)
            i = i + 1
        i = 0

        # 1 União
        uniao = (set(conjunto1).union(conjunto2))

        # 2 Essa operação é muito útil quando precisamos descobrir elementos que duas listas possuem em comum:
        intersecao = (set(conjunto1).intersection(conjunto2))

        # 3 A diferença entre dois conjuntos A e B retorna somente os elementos de A que não estão em B, ou seja, retira de A todos os elementos comuns a ambos os conjuntos:
        diferenca1 = (set(conjunto1).difference(conjunto2))
        diferenca2 = (set(conjunto2).difference(conjunto1))

        # 4 Diferença simétrica é uma operação sobre os dois conjuntos, que retorna todos os elementos (de ambos os conjuntos a e b) que pertencem a somente um dos conjuntos.
        simetrica1 = (set(conjunto1).symmetric_difference(conjunto2))

        # 5 Também podemos verificar se um conjunto é um subconjunto de 
        subconjunto1 = set(conjunto1).issubset(conjunto2)
        subconjunto2 = set(conjunto2).issubset(conjunto1)


        # 6 Superconjunto
        superconjunto1 = set(conjunto1).issuperset(conjunto2)
        superconjunto2 = set(conjunto2).issuperset(conjunto1)

        print('Dados os conjuntos A:',conjunto1,'e B:',conjunto2)
        print('1- A união entre A U B é: ',uniao)
        print('2- A interseção entre A ∩ B é:',intersecao)
        print('3- A diferença de A com B é:',diferenca1)
        print('4- A diferença de B com A é:',diferenca2)
        print('5- A diferença simétrica entre A △ B é:',simetrica1)

        if subconjunto1 == True:
            print('6- O conjunto A é Subconjunto de B')
        if subconjunto1 == False:
            print('6- O conjunto A não é Subconjunto de B')
        if subconjunto2 == True:
            print('7- O conjunto B é Subconjunto de A')
        if subconjunto2 == False:
            print('7- O conjunto B não é Subconjunto de A')

        if superconjunto1 == True:
            print('8- O conjunto A é Superconjunto de B')
        if superconjunto1 == False:
            print('8- O conjunto A não é Superconjunto de B')
        if superconjunto2 == True:
            print('9- O conjunto B é Superconjunto de A')
        if superconjunto2 == False:
            print('10- O conjunto B não é Superconjunto de A')
        obrigado()
    elif resp == 2:
        print('| 2 - Olhando as Matrizes -  Funcional, Injetora, Total, Subjetora             |')
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
            print('Sua matriz tem relação FUNCIONAL.')
        else:
            funcional = (False)
        
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
            print('Sua matriz tem relação INJETORA.')
        else:
            injetora = (False)

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
            print('Sua matriz tem relação TOTAL.')
        else:
            total = (False)


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
            print('Sua matriz tem relação SUBREJETORA.')
        else:
            subrejetora = (False)

        #Monomorfismo
        if injetora == (True) and total == (True):
            monomorfismo = True
            print('Sua matriz é MONORMOFA.')
        else:
            monomorfismo = False

        #Epimorfismo
        if funcional == (True) and subrejetora == (True):
            epimorfismo = True
            print('Sua matriz é EPIMORFA.')
        else:
            epimorfismo = False
        obrigado()
        #Isomorfismo
        #print('Isomorfismo ??')

    elif resp == 3:
        print('| 3 - Matrizes - Reflexiva, Irreflexiva, Simetrica, Anti-simétrica.            |')
        numero_de_linhas = 3
        numero_de_colunas = 3
        matriz = []
        for i in range(numero_de_linhas):
            linhas = []
            for j in range(numero_de_colunas):
                num = int(input('Digite o elemento {} X {} : '.format(i, j)))
                linhas.append(num)
            matriz.append(linhas)

        # Exibir Matriz
        numero_de_linhas = len(matriz)
        numero_de_colunas = len(matriz[0])
        print('Sua matriz {} X {} tem os seguuntes números:'.format(numero_de_linhas, numero_de_colunas))
        for i in range(numero_de_linhas):
            for j in range(numero_de_colunas):
                # %3d define qual tamanho da distancia
                print("%3d" % (matriz[i][j]), end="")
            # pule uma linha
            print()

        # Reflexiva
        if matriz[0][0] == 1 and matriz[1][1] == 1 and matriz[2][2] == 1:
            reflexiva = True
            print('Sua matriz é REFLEXIVA')

        # Ireflexiva
        if matriz[0][0] == 0 and matriz[1][1] == 0 and matriz[2][2] == 0:
            irreflexiva = True
            print('Sua matriz é IRREFLEXIVA')

        # Simetrica
        if matriz[0][1] == matriz[0][2] == matriz[1][2] == matriz[1][0] == matriz[2][0] == matriz[2][1]:
            simetrica = True
            print('Sua matriz é SIMÉTRICA')

        # Anti-Simétrica ou Assimétrica
        if matriz[0][1] != matriz[1][0] or matriz[0][1] != matriz[2][0] or matriz[0][1] != matriz[2][1] or matriz[0][2] != matriz[1][0] or matriz[0][2] != matriz[2][0] or matriz[0][2] != matriz[2][1] or matriz[1][2] != matriz[1][0] or matriz[1][2] != matriz[2][0] or matriz[1][2] != matriz[2][1]:
            print('Sua matriz é ANTI-SIMÉTRICA')
        # Transitiva
        if matriz[0][0]==1 and matriz[0][0] == matriz[0][1] == matriz[1][1] or matriz[0][1]==1 and matriz[0][1] == matriz[0][2] == matriz[1][2] or matriz[1][0]==1 and matriz[1][0] == matriz[1][1] == matriz[2][1] or matriz[1][1]==1 and matriz[1][1] == matriz[1][2] == matriz[2][2]:
            print('Sua matriz é TRANSITIVA')
        obrigado()
    else:
        print('ERRO DE ÍNDICE')
        obrigado()

menu()


