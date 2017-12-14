'''6. Data por extenso.
    Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima
    a data com o nome do mês por extenso.'''

meses = 'janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'
data = input("Digite a data de seu aniversário: dd/mm/aaaa ")
#É preciso tratar os dados
tratamento = (data.split('/'))
i = (int(tratamento[1]) - 1)
print('Você nasceu em {} de {} de {}.'.format(tratamento[0],meses[i],tratamento[2]))
