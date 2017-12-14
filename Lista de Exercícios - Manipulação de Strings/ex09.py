'''9. Jogo de Forca.
    Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo
    texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
    Digite uma letra: A'''

print(' * JOGO DA FORCA * ')

palavra = ['d','a','n','i','e','l']
letras_descobertas = []
r = 1
for i in range(0, len(palavra)):
    letras_descobertas.append('_')

acertou = False

#while acertou == False:
while r <= 6:
    letra = str(input('Digite a letra: '))
    r = r + 1
    for i in range(0, len(palavra)):
        if letra == palavra[i]:
            letras_descobertas[i] = letra
    acertou = True
    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == '-':
            acertou = False

    print('A palavra é:',letras_descobertas)
