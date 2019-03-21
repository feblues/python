from random import choice
from time import sleep
import emoji
print('*-*-'*7)
print('Vamos jogar jokenpo?')
print('*-*-'*7)

print('Escolha sua opcao: ')
print('1 para PEDRA')
print('2 para PAPEL')
print('3 para TESOURA')
us = int(input('Pedra, Papel ou Tesoura: '))
print('Vez do computador escolher ')
print('Carregando...')
sleep (2)
lista = [1, 2, 3]
cpu = choice(lista)
if cpu == us:
    print ('Voces empataram!!')
elif 1 == us and cpu == 3:
    print('Voce escolheu pedra e o cpu escolheu tesoura')
    print('Voce venceu!!!!')
elif 2 == us and 1 == cpu:
    print('Voce escolheu papel e o cpu escolheu pedra')
    print('Voce venceu!!!!')
elif 3 == us and 2 == cpu:
    print('Voce escolheu tesoura e o cpu escolheu papel')
    print('Voce venceu!!!!')
elif 1 == us and 2 == cpu:
    print('Voce escolheu pedra e o cpu escolheu papel')
    print('Voce perdeu!!!!')
elif 2 == us and 3 == cpu:
    print('Voce escolheu papel e o cpu escolheu tesoura')
    print('Voce perdeu!!!!')
elif 3 == us and 1 == cpu:
    print('Voce escolheu tesoura e o cpu escolheu pedra')
    print('Voce perdeu!!!!')
elif us > 3:
    print('Voce escolheu uma opcao nao disponivel. Reinicie o Game!!!')