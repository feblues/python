print ('--'*10)
print ('Emprestimo de casa')
print ('--'*10)
val = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o seu salario: R$ '))
ano = int(input('Digite quantos anos quer pagar: '))
prest = val / (ano * 12)
porc = (prest / sal) * 100
if porc < 31:
    print ('Emprestimo foi aprovado')
    print ('A prestacao utilizara aproximadamente {:.0f}% do seu salario'.format(porc+1))
else:
    print ('Emprestimo negado, a prestacao é superior a 30% do seu salario')
    print('A prestacao utilizara aproximadamente {:.0f}% do seu salario!! \33[7;30mAumente a quantidade de anos!!!\33[m'.format(porc + 1))