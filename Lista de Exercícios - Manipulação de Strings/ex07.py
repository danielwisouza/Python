'''7. Conta espaços e vogais.
    Dado uma string com uma frase informada pelo usuário (incluindo espaços em
    branco), conte:
        a. quantos espaços em branco existem na frase.
        b. quantas vezes aparecem as vogais a, e, i, o, u.'''
frase = input('Digite qualquer coisa: ')

#Deixar tudo em minusculo para contar a quantidade de letras
#se Ana duas letras A
frase = frase.lower()

branco = frase.count(' ')
a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

print('A frase informada tem {} espaços em branco.'.format(branco))
print('A letra A aparece {} vezes.'.format(a))
print('A letra E aparece {} vezes.'.format(e))
print('A letra I aparece {} vezes.'.format(i))
print('A letra O aparece {} vezes.'.format(o))
print('A letra U aparace {} vezes.'.format(u))
