''' 7. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
quadrados dos elementos do vetor.'''

vetor = []
i = 0
soma = 0
while i < 10:
    numero = int(input('Digite número: '))
    vetor.append(numero)
    soma = soma + numero
    i = i + 1
quadrado = soma**2
print('Os valores digitados foram: ',vetor)
print('A soma dos valores é',soma)
print('O quadrado da soma desses números é',quadrado)

