'''8. Número por extenso.
    Escreva um programa que solicite ao usuário a digitação de um número até 99 e
    imprima-o na tela por extenso.'''
unidade = ['','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez']
dez = ['','onze','doze','treze','quatorce','quinze','dezesseis','dezessete','dezoito','dezenove']
dezena = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']

numero = int(input('Digite um número: '))

if numero <= 10:
    print(unidade[numero])
elif numero > 10 and numero <= 19:
    numero = (numero - 10)
    print(dez[numero])
elif numero >= 20 and numero < 100:
    c = str(numero)
    numero = ('').join(c)
    c = int((numero[0]))
    d = int((numero[1]))
    c = c - 2
    print(dezena[c],'e' ,unidade[d])