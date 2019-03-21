print ('Programa para ler 3 numeros e informar o maior')
print (' ')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
l = [n1,n2,n3]
max = max(l)
min = min(l)
print ('O valor maior é {} e o menor é {}'.format(max,min))