from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
cpu = randint(0,2)
print('O computador escolheu {}'.format(itens[cpu]))
print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
uso = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*10)
print('Computador jogou {} '.format(itens[cpu]))
print('Jogador jogou {} '.format(itens[uso]))
print('-='*10)
if cpu == 0:
    if uso == 0:
        print('EMPATE')
    elif uso == 1:
        print('Jogador VENCEU!!!')
    elif uso == 2:
        print('CPU VENCEU!!!!')
    else:
        print('Opcao Invalida')
elif cpu == 1:
    if uso == 0:
        print('CPU VENCEU!!!!')
    elif uso == 1:
        print('EMPATE')
    elif uso == 2:
        print('Jogador VENCEU!!!')
    else:
        print('Opcao Invalida')
elif cpu == 2:
    if uso == 0:
        print('Jogador VENCEU!!!')
    elif uso == 1:
        print('CPU VENCEU!!!!')
    elif uso == 2:
        print('EMPATE')
    else:
        print('Opcao Invalida')