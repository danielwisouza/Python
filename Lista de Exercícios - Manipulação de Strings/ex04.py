'''4. Nome na vertical em escada.
    Modifique o programa anterior de forma a mostrar o nome em formato de
    escada.'''

nome = input('Digit seu nome: ')
i = 0
while i <= (len(nome)):
    print(nome[:i])
    i = i + 1

