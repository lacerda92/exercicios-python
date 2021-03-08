#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('======BEM VINDO AO MERCADO DO EDU======')
preco = float(input('Valor original do produto é de: '))
desconto = preco*0.05
precofinal = preco-desconto
print('O produto possui desconto promocional de 5%, que é de: {:.2f}.'.format(desconto))
print('O valor final do produto é de: {:.2f}.'.format(precofinal))
print('Muito obrigado!')



#exemplo
#10% de 1750
#1750*15/100
#175


#outra forma de realizar a ativdade

"""preço = float(input('Valor original do produto? R$ '))
desconto = preço*5/100
preçofinal = preço-desconto
print('O desconto do produto atualmente é de 5%, o que equivale a: R${:.2f}'.format(desconto))
print('O valor do produto, já somado ao desconto promocional é de: R${:.2f}'.format(preçofinal))"""