#crie um programa que leia um número real qualquer pelo teclado e msotre na tela a sua porção inteira.

#ex: digite um número: 6.127
#o número 6.127 tem a parte inteira 6.

from math import trunc
numero = float(input('Digite um número: '))
parteinteira = trunc(numero)
print('A parte inteira do número {} é: {} '.format(numero,parteinteira))

import math
numero = float(input('Digite um número: '))
parteinteira = math.trunc(numero)
print('A parte inteira do número {} é: {}'.format(numero,parteinteira))