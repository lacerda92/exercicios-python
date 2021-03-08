#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado, e a quantidade de dias pelos quais ele foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

print('=====BEM VINDO A EDU RENT CARS=====')
km = float(input('Quantos km você dirigiu desde de que pegou o veículo conosco? '))
dias = float(input('Quantos dias você ficou com um de nossos carros? '))
aluguel = (0.15*km)+(60*dias)
print('O valor a ser pago pelo carro é de: R${:.2f}'.format(aluguel))
print('=====MUITO OBRIGADO=====')