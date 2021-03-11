#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido


import random
aluno1 = input('NOME DO ALUNO: ')
aluno2= input('NOME DO ALUNO: ')
aluno3 = input('NOME DO ALUNO ')
aluno4 = input('NOME DO ALUNO ')
população = (aluno1,aluno2,aluno3,aluno4)
sorteio = random.choices(população)
print('=====O GRANDE ALUNO SORTEADO PARA FAZER O MEU TRABALHO, FOI: {}'.format(sorteio))


#OUTRO METODO
import random
aluno1 = str(input('NOME DO ALUNO: ')) #não é obrigatório sinalizar o uso de string
aluno2 = str(input('NOME DO ALUNO: '))
aluno3 = str(input('NOME DO ALUNO: '))
aluno4 = str(input('NOME DO ALUNO: '))
universo = [aluno1,aluno2,aluno3,aluno4] #universo é uma LISTA, quantidade de itens que eu quero, ficam dentro dos colchetes
sorteio = random.choice(universo)
print('O Aluno escolhido foi: {}'.format(sorteio)

#METODO CURTO
from random import choice
aluno1 = input('NOME DO ALUNO: ')
aluno2 = input('NOME DO ALUNO: ')
aluno3 = input('NOME DO ALUNO: ')
aluno4 = input('NOME DO ALUNO: ')
lista = [aluno1,aluno2,aluno3,aluno4]
sorteio = choice(lista)
print('O aluno sorteado foi: {}'.format(sorteio))