#tipos de primitivos
#int = número inteiros = 7,5,-5,-10,56484
#float = números reais ou números de ponto flutuante = 4.5, 55.2, 3.2, 7.0
#bool = valores lógicos ou boleanos = True, False
#str = caracteres ou strings = 'Ola', '7.5', '', 'bunda lele'

#004
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela
n1 = input('Digite qualquer coisa: ')
print('A classe de {} é: '.format(n1), type(n1))
"""print(n1,'está todo minúscula? ', n1.islower())
print(n1, 'é uma letra do alfabeto? ', n1.isalpha())
print(n1, 'é um número? ', n1.isnumeric())
print(n1, 'está todo maiúscula? ',n1.isupper())
print(n1,"é um decimal? ",n1.isdecimal())"""

print('{} está todo minúscula? '.format(n1), n1.islower())
print('{} é uma letra do alfabeto (somente possui letras)? '.format(n1), n1.isalpha())
print('{} é um número? '.format(n1), n1.isnumeric())
print('{} está todo em maiúsculo? '.format(n1),n1.isupper())
print('{} é um decimal? '.format(n1), n1.isdecimal())
print('{} só tem espaços? '.format(n1), n1.isspace()) #não é em branco, é literalmente ESPAÇO
print('{} é alphanumérico? (possui letras e números) '.format(n1),n1.isalnum())
