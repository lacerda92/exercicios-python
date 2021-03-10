#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
angulo = float(input('Digite ângulo que deseje saber o SENO, COSSENO e a TANGENTE: '))
radianos = math.radians(angulo) #primeiro você converte o angulo em RADIANOS
SENO = math.sin(radianos)    #ambos os resultados são calculados em radianos.
COSSENO = math.cos(radianos)
TANGENTE = math.tan(radianos)
print('O seno do ângulo {} é igual a: {:.2f}.'.format(angulo,SENO))
print('O cosseno do ângulo {} é igual a: {:.2f}.'.format(angulo,COSSENO))
print('A tangente do ângulo {} é igual a: {:.2f}'.format(angulo,TANGENTE))

#outro metodo
import math
angulo = float(input('Digite o ângulo para saber o SENO, COSSENO e a TANGENTE: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo {} possui SENO: {:.2f}, COSSENO: {:.2f} e TANGENTE: {:.2f}'.format(angulo,seno,cosseno,tangente))

#outro metodo mais curto
from math import sin,cos,tan,radians
angulo = float(input('Digite o ângulo para saber o SENO, COSSENO e a TANGENTE: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {} possui SENO: {:.2f}, COSSENO: {:.2f} e TANGENTE: {:.2f}'.format(angulo,seno,cosseno,tangente))
