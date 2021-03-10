#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule a mostre o comprimento da hipotenusa

import math
CA = float(input('Qual o tamanho do cateto adjacente? '))
CO = float(input('Qual o tamanho do cateto oposto? '))
H1 = (CA**2+CO**2)
H2 = math.sqrt(H1)
print('A HIPOTENUSA deste triangulo, que possui CA: {}, e CO {} é igual a: {:.2}'.format(CA,CO,H2))


#usando a função de cálculo de hipotenusa da biblioteca de matemática.

import math
CA = float(input('Qual o tamanho do cateto adjacente? '))
CO = float(input('Qual o tamanho do cateto oposto? '))
H = math.hypot(CA,CO)
print('A HIPOTENUSA deste triangulo, que possui CA: {}, e CO: {} é igual a: {:.2f}'.format(CA,CO,H))

#metodo de resolução sem importação nenhuma

CA = float(input('Qual o tamanho do cateto adjacente? '))
CO = float(input('Qual o tamanho do cateto oposto? '))
H = (CA**2+CO**2)**(1/2)
print( 'A HIPOTENUSA deste triângulo vai medir: {:.2f}'.format(H))

#metodo importando somente a formula que vamos usar

from math import hypot
CA = float(input('Qual o tamanho do cateto adjacente? '))
CO = float(input('Qual o tamanho do cateto oposto? '))
print('A HIPOTENUSA deste triângulo vai medir :{:.2f}'.format(hypot(CA,CO)))
