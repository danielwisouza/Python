''' 2. Agora usando listas, indique como um troco deve ser dado utilizando-se um número mínimo de
notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado
desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1
reais, e que nenhuma delas esteja em falta no caixa.'''

notas = [50,20,10,5,2,1]
cont = []
pagar = float(input('Digite valor da compra: R$ '))
pago = float(input('Digite valor pago: R$ '))
#Eu preciso falar que 'troco' tem que ser inteiro para aceitar valores com ponto.
troco = int((pago - pagar))
i = 0

print('Seu troco é R$ {:.2f}'.format(troco))
while troco > 0:
    #Eu preciso falar que 'n' tem que ser inteiro
    n = int(troco/notas[i])
    troco = troco%notas[i]
    if int(n) != 0:
        print('{} notas de {}'.format(n, notas[i]))
    i=i+1

print('Obrigado por comprar com a gente!!!')
