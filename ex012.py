n = float(input('Informe o preco do produto em R$ '))
de = float(input('Informe o desconto % '))
fi = n - ((n / 100) * de)
print ('O valor do produto com desconto é: R$ {:.2f}'.format(fi))