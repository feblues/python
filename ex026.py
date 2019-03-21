frase = str(input('Digite uma frase: ')).upper().strip()from random import choice
n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)
print ('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print ('A primeira letra A apareceu na posicao {}.'.format(frase.find('A')+1))
print ('A ultima letra A apareceu na posicao {}.'.format(frase.rfind('A')+1))