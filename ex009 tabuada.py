#faça um programa que leia um número INTEIRO qualquer e mostra na tela a sua tabuada.
print('Olá, eu consigo calcular a tabuada de QUALQUER número, você consegue acreditar nisso?')
"""numero = int(input('Digite um número: '))
x1 = numero*1
x2 = numero*2
x3 = numero*3
x4 = numero*4
x5 = numero*5
x6 = numero*6
x7 = numero*7
x8 = numero*8
x9 = numero*9
x10 = numero*10

print('Estou calculando o seu resultado, aguardo: ')
print('')
print('')
print('')
print('Prontinho')
print('A tabuada do número {:=^11}, indo de 1 a 10 é:'.format(numero))
print('---------------')
print(numero,'x 1 = {}'.format(x1))
print(numero,'x 2 = {}'.format(x2))
print(numero,'x 3 = {}'.format(x3))
print(numero,'x 4 = {}'.format(x4))
print(numero,'x 5 = {}'.format(x5))
print(numero,'x 6 = {}'.format(x6))
print(numero,'x 7 = {}'.format(x7))
print(numero,'x 8 = {}'.format(x8))
print(numero,'x 9 = {}'.format(x9))
print(numero, 'x 10 = {}'.format(x10)) 
print('---------------')"""

#outra forma de realizar essa atividade (somente a parte dos calculos)
numero = int(input('Digite um número: '))
print('-'*15)
print('{} x {:2} = {}'.format(numero,1,numero*1))
print('{} x {:2} = {}'.format(numero,2,numero*2))
print('{} x {:2} = {}'.format(numero,3,numero*3))
print('{} x {:2} = {}'.format(numero,4,numero*4))
print('{} x {:2} = {}'.format(numero,5,numero*5))
print('{} x {:2} = {}'.format(numero,6,numero*6))
print('{} x {:2} = {}'.format(numero,7,numero*7))
print('{} x {:2} = {}'.format(numero,8,numero*8))
print('{} x {:2} = {}'.format(numero,9,numero*9))
print('{} x {} = {}'.format(numero,10,numero*10)) #pra corrigir o distanciamento provocado pelo numero 10, é só usar {:2}
print('-'*15)