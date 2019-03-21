print ('Programa para validar se e possivel formar um triangulo')
print (' ')
r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))
list = [r1, r2, r3]
maior = max(list)
menor = min(list)
meio = (r1 + r2 + r3) - (maior + menor)
calculo = meio + menor
if calculo > maior:
    print ('É possivel formar um triangulo')
else:
    print ('Não é possivel formar um triangulo')