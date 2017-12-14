''' 4. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

aluno = []
aluno_nota = []
lista_media = []
cont7 = 0
i=0
while i < 1:
    soma = 0
    nome = (input('Digite nome do {}º aluno: '.format(i)))
    aluno.append(nome)
    n = 0
    while n < 4:
        nota = float(input('Digite {}º nota do aluno: '.format(n)))
        aluno_nota.append(nota)
        soma = soma + nota
        n = n + 1
    media = soma/4
    lista_media.append(media)
    if media >= 7:
        cont7 = cont7 + 1
    i = i + 1

print('\nMédia de todos os alunos:',lista_media)
print('Totalizando temos {} alunos com media final Igual ou maior que 7'.format(cont7))






