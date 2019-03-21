print ('-'*15)
print ('Programa para comparar numeros')
print ('-'*15)
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite mais um numero inteiro: '))
if n1 > n2:
    print ('O \33[7;30mprimeiro\33[m valor digitado é maior!!!!!')
elif n2 > n1:
    print ('O \33[7;30msegundo\33[m valor digitado é o maior!!!!')
else:
    print ('Os numeros digitados sao \33[7;30miguais\33[m !!!!!!!')