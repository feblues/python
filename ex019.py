from random import choice
a1 = input('Digite o primeiro aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
lista = [a1,a2,a3,a4]
e1 = choice(lista)
print ('O escolhido foi {}'.format(e1))