''' 10.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em
uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro,
2 – Fevereiro, . . . )'''

temp = []
mes = ['1 – Janeiro','2 - Fevereiro','3 - Março ','4 - Abil','5 - Maio','6 - Junho','7 - Julho','8 - Agosto','9 - Setembro','10 - Outubro','11 - Novembro','12 - Dezembro']
i = 0
soma = 0
while i < 12:
    c = float(input('Digite a temperatura do mês de {} em Cº: '.format(mes[i])))
    temp.append(c)
    soma = soma + c
    i = i + 1
media = soma / 12
i = 0
print('A média anual das temperaturas: {:.2f} Cº\n'.format(media))
print('Temperaturas acima da média anual e em que messes elas ocorreram: ')
while i < 10:
    if temp[i] > media:
        print(mes[i],'{} Cº'.format(temp[i]))
    i = i + 1
