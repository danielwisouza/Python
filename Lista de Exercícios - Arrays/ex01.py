''' 1. Leia um vetor de 10 elementos e calcule o maior e o menor valor'''

valor = []
maior = 0
menor = 100000000
i = 0
while i < 10:
    n = int(input('Digite número: '))
    valor.append(n)
    if (valor[i] > maior):
        maior = valor[i]

    if (valor[i] < menor):
        menor = valor[i]
    i = i + 1

print('Os valores digitados foram: ',valor)
print('O maior valor entre eles é o: ',maior)
print('O menor valor entre eles é o: ',menor)




