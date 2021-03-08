#faça um programa que leia a largura e a altura de uma parede em metros, calcule a
# sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro(1) de tinta pinta uma área de 2m²

"""largura = int(input('Digite a largura da parede que você deseja pintar(em metros): '))
altura = int(input('Digite a altura da parede que você deseja pintar(em metros): '))
areatotal = largura*altura
tinta = areatotal/2
print('A largura da sua parede é de: {}, a altura é de: {}, portanto a área total é de {} metros quadrados'.format(largura,altura,areatotal))
print('Você vai precisar de {} litros de tinta para realizar a sua pintura'.format(tinta))"""

#outra forma de realizar usando float (flutuação do ponto  e virgula)
largura = float(input('Digite a largura da parede que você deseja pintar(em metros): '))
altura = float(input('Digite a altura da parede que você deseja pintar(em metros): '))
areatotal = largura*altura
tinta = areatotal/2
print('A largura da sua parede é de: {}, a altura é de: {}, portante a área total é de: {:.2f} metros quadrados.'.format(largura,altura,areatotal))
print('Você vai precisar de {:.2f} litros de tinta para realizar a sua pintura.'.format(tinta))