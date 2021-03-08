#003
#crie um programa que leia dois números e mostra a soma entre ele.
n1 = int(input('Digite um valor: ')) #é preciso por INT no início,pois é um número inteiro, caso contrario, não vai somar, vai juntar os itens exem: 5+5 = 55
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma dos valores; {} e {} é {}!'.format(n1, n2, soma))