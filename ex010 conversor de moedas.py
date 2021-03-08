#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere 1,00 USS = 3,27 RS
carteira = float(input('Quanto dinheiro você tem em REAL? R$'))
dolar = carteira/3.27
print('O dólar esta custando RS 3,27')
print('Com o valor que você tem atualmente,R${:.2f} , usando uma conversão direta, dá pra comprar USS{:.2f} dólares'.format(carteira,dolar))


#convertendo de dolar para real

carteira2 = float(input('Quantos dolares vocês tem? USS'))
real = carteira2*3.27
print('Com o real (R$) valendo 0,30 (em conversão direta e arredondada), você podera comprar {:.2f} reais'.format(real))
