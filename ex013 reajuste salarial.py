#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('=====BEM VINDO=====')
print('EDUARDO LACERDA CONTABILIDADE     CFC 123456')
salario = float(input('Salário atual: '))
aumento = salario*0.15
salariofinal = salario+aumento
print('O aumento de 15% equivale: {:.2f}.'.format(aumento))
print('Portanto, o seu salario final é de: {:.2f}'.format(salariofinal))
print('=====OBRIGADO=====')




#outra forma de realizar a atividade
"""salario = float(input('O salarioa atual é de: R$ '))
aumento = salario*15/100
salariofinal = salario+aumento
print('O salário final, após o aumento, é de: R${:.2f}'.format(salariofinal))"""