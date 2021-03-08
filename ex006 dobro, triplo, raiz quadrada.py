#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""numero =int(input('Digite um número: '))
print('O dobro do número {} é:'.format(numero),numero*2,'o triplo do número {} é:'.format(numero),numero*3,'e a raiz quadrada '
'do número {} é:'.format(numero),numero**(1/2))"""

#outra maneira de realizar essa tarefa
numero =int(input('Digite um número: '))
dobro = numero*2
triplo = numero*3
raiz2 = numero**(1/2)
print("O dobro é igual {}, \nO triplo é igual {} \nE a raiz quadrada é igual a {:.2f}".format(dobro,triplo,raiz2))

#o codigo .2f serve para indicar duas casas após a vírgula, é um comando float
# \n serve para pular uma linha!
# a raíz quadrada também pode ser calculada com a função pow
#exemplo usand pow


print('A raíz cubida do numero {} é igual a: {:.2f}. '.format(numero,pow(numero,1.3)))

