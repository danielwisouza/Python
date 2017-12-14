''' 3. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

import random
mestre = []
par = []
impar = []
i = 0
print('Gerando valores aleatórios com RANDOM...............')
while i <= 20:
    
    #n = int(input('Digite valor: '))
    #mestre.append(n)

    #Gerando valores aleatórios com RANDOM de 1 até 100
    mestre.append(random.randint(1,100))

    if mestre[i] % 2 == 0:
        par.append(mestre[i])
    else:
        impar.append(mestre[i])
    i = i + 1
print('Os 20 valores digitados são: ',mestre)
print('Os valores pares são: ',par)
print('Os valores impares são: ',impar)
