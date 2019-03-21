sal = float(input('Digite o seu salario R$ '))
por = float(input('Informe o percentual de aumento em % '))
fin = sal + ((sal / 100) * por)
print ('Parabens!!! Seu novo salário é de R$ {:.2f}'.format(fin))