'''1. Tamanho de strings.
    Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
    Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

string1 = input('Digite algo: ')
string2 = input('Digite algo: ')
print('String1 = {} : {} caracteres'.format(string1,(len(string1))))
print('String2 = {} : {} caracteres'.format(string2,(len(string2))))

if (len(string1) == len(string2)):
    print('As duas strings são do mesmo tamanho.')

elif (len(string1) != len(string2)):
    print('As duas strings são de tamanhos diferentes.')

if (string1 == string2):
    print('A string1 {} é igual no conteudo da string2 {}.'.format(string1,string2))

elif (string1 != string2):
    print('A string1 : -> {} <- é diferente no conteudo da string2 : -> {} <- .'.format(string1,string2))
