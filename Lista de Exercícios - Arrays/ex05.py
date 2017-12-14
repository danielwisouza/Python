''' Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
os números.'''
vetor = []
i = 0
soma = 0
while i < 5:
    numero = int(input('Digite numero: '))
    vetor.append(numero)
    soma = soma + numero
    i = i + 1
mult = vetor[0]*vetor[1]*vetor[2]*vetor[3]*vetor[4]
print('Os valores digitados foram: ',vetor)
print('A soma dos valores é',soma)
print('A multiplicação dos valores é',mult)