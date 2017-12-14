''' 6. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

pessoas = ['Daniel', 'Isabella', 'Jõao', 'Maria', 'Guilherme']
idade_pessoas = []
altura_pessoas = []
i = 0
while i < 5:
    #nome = input('Nome da pessoa: ')
    #pessoas.append(nome)
    idade = int(input('Idade da pessoa: '))
    idade_pessoas.append(idade)
    altura = float(input('Altura da pessoa: '))
    altura_pessoas.append(altura)
    i = i + 1

print('Ordem correta Pessoas:     ',pessoas)
print('Ordem correta Idade: ',idade_pessoas)
print('Ordem correta Altura: ',altura_pessoas)
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('Inversão de Pessoas',pessoas[::-1])
print('Inversão de Idade',idade_pessoas[::-1])
print('Inversão de Altura:   ',altura_pessoas[::-1])