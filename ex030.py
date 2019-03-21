print ('Programa que valida numero par ou impar')
n = int(input('Digite um numero: '))
r = n % 2
if r == 0:
    print ('O numero {} é par'.format(n))
else:
    print ('O numero {} é impar'.format(n))
