print('-'*45)
print ('Programa para validar se e possivel formar um triangulo')
print('-'*45)
print (' ')
r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))
list = [r1, r2, r3]
maior = max(list)
menor = min(list)
meio = (r1 + r2 + r3) - (maior + menor)
calculo = meio + menor
if calculo > maior and maior == menor and menor == meio:
    print('Possivel formar um triangulo Equilatero')
elif calculo > maior and maior == menor or menor == meio:
    print ('Possivel formar um triangulo Isosceles')
elif calculo > maior and maior != menor and maior != meio or menor != meio and menor != maior:
    print('Possivel formar um triangulo Escaleno')
else:
    print ('Não é possivel formar um triangulo')