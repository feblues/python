from datetime import date
print ('Programa para calculo do ano bissexto')
print (' ')
ano = int(input('Digite um ano ou 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print ('{} é um ano bissexto'.format(ano))
else:
    print ('{} não é um ano bissexto'.format(ano))