#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""nota1 = int(input("Digite a nota da sua primeira avaliação: "))
nota2 = int(input('Digite a nota da sua segunda avaliação: '))
soma = nota1+nota2
media = soma/2
print('A média da sua nota é: {}'.format(media))"""


n1 = float(input('Sua nota na primeira avaliação: '))
n2 = float(input('Sua nota na segunda avaliação: '))
soma = n1+n2 #aqui eu poderia ter colocado assim: média = (n1 + n2) /2 ( é preciso por no parentese porque se não o calculo vai dar o resultado errado, já que soma e subtração fica por ultimo
media = soma/2  #a soma é dividida pela quantidade de provas que houveram
print('A média geral de suas notas foi de: {}.'.format(media))
print('VAI ESTUDAR PROGRAMAÇÃO SEU VAGABUNDO')
