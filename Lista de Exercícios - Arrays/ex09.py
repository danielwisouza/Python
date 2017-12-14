''' 9. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

import random
aluno = []
idade = []
i = 0
r = 0
soma = 0
cont_altura = 0
while i < 30:
    #altura = float(input('Altura: '))
    #aluno.append(altura)

    #Retorna valores aleatórios decimais entre 1.0 e 2.0
    aluno.append(random.uniform(1.0,2.0))

    #idada_aluno = int(input("Idade: "))
    #idade.append(idada_aluno)

    #Retorna valores aleatórios Inteiro entre 1 e 50
    idade.append(random.randint(1,50))

    soma = soma + aluno[i]
    i = i + 1

media = float(soma / 30)
while r < 30:
    if idade[r] > 13:
        if aluno[r] < (media):
            cont_altura = cont_altura + 1
    r = r + 1

#Saída
print('Altura de todos os aluno:',aluno)
print('Média das alturas: {:.2f}'.format(media))
print('Idade de todos os aluno:',idade)
print('Existem {} com mais de 13 anos que possuem altura inferior à média de altura desses alunos que é {:.2f}'.format(cont_altura,media))
