from datetime import date
print ('-'*45)
print ('Programa para calcular ano de alistamento')
print ('-'*45)
ano_nas = int(input('Digite o ano que voce nasceu: '))
ano_atu = date.today().year
idade = ano_atu - ano_nas
if idade > 18:
    idade = idade - 17
    print('Voce já passou do prazo do alistamento em {} anos!!!!!'.format(idade))
elif idade < 16:
    idade = 17 - idade
    print('Ainda falta(m){} ano(s) para se alistar!!!!'.format(idade))
else:
    print('É hora de se alistar!!!!')