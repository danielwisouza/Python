''' 8. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros
vetores.'''
vetor1 = []
vetor2 = []
new_vetor = []
i = 0

while i < 11:
    numero = int(input("Valor {}º do Vetor 1 : ".format(i)))
    vetor1.append(numero)
    numero1 = int(input("Valor {}º do Vetor 2 : ".format(i)))
    vetor2.append(numero1)

    #Novo vetor recebe vetor1 e vetor2
    new_vetor.append(vetor1[i])
    new_vetor.append(vetor2[i])
    i = i + 1

print('Elementos do primeiro vetor:',vetor1)
print('Elementos do Segundo vetor',vetor2)
print('Novo vetor Junção -> Primeiro + Segundo <- intercalados:',new_vetor)
