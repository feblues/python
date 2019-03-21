print('-'*25)
print('Calculo Media do Aluno')
print('-'*25)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m <= 5:
    print('Voce foi \33[4;34mREPROVADO\33[m sua média foi de {:.2f}'.format(m))
elif m > 5 and m <=6.9:
    print('Voce esta de \33[4;35mRECUPERACAO\33[m sua média foi de {:.2f}'.format(m))
else:
    print('Voce foi \33[4;36mAPROVADO\33[m sua média foi de {:.2f}'.format(m))
