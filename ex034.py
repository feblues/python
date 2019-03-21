print ('Programa para calculo aumento de salario')
print (' ')
sal = float(input('Digite seu salario em R$ '))
if sal > 1250.00:
    print ('Voce recebeu um aumento de 10%. Seu novo salario é de R$ {:.2f}'.format(((sal / 100)* 10)+ sal))
else:
    print('Voce recebeu um aumento de 15%. Seu novo salario é de R$ {:.2f}'.format(((sal / 100) * 15) + sal))
