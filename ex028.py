from random import choice
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
cpu = choice(lista)
us = int(input('Digite um numero de 0 a 5: '))
print ('Processando.....')
sleep(2)
if cpu == us:
    print ('Voce escolheu {} e o CPU escolheu {}'.format(us, cpu))
    print ('Voce descobriu! You WIN!!!!!!')
else:
    print ('Voce escolheu {} e o CPU escolheu {}'.format(us,cpu))
    print ('You Lose!!!!!!!')