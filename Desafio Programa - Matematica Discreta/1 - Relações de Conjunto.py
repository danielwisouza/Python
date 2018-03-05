print('|-------------------------------------------------------------------|')
print('|         EASY DISCRETE MATHEMATICS - Relações de Conjunto          |')
print('|    Daniel Willians Ignacio de Souza - 1º Semestre Banco de Dados  |')
print('|            Professor: Marcos Allan Ferreira Goncalves             |')
print('|-------------------------------------------------------------------|')
print('1 - Relações de Conjunto')
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

print('\n')
print('Dados os conjuntos A:',conjunto1,'e B:',conjunto2)
print('\n')
print('A união entre A U B é: ',uniao)
print('A interseção entre A ∩ B é:',intersecao)
print('A diferença de A com B é:',diferenca1)
print('A diferença de B com A é:',diferenca2)
print('A diferença simétrica entre A △ B é:',simetrica1)

if subconjunto1 == True:
    print('O conjunto A é Subconjunto de B')
if subconjunto1 == False:
    print('O conjunto A não é Subconjunto de B')
if subconjunto2 == True:
    print('O conjunto B é Subconjunto de A')
if subconjunto2 == False:
    print('O conjunto B não é Subconjunto de A')
if superconjunto1 == True:
    print('O conjunto A é Superconjunto de B')
if superconjunto1 == False:
    print('O conjunto A não é Superconjunto de B')
if superconjunto2 == True:
    print('O conjunto B é Superconjunto de A')
if superconjunto2 == False:
    print('O conjunto B não é Superconjunto de A')
