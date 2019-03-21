n = float(input('Quanto dinheiro voce possui na carteira? R$ '))
d = float(input('Cotação do dolar atual: $ '))
conv = n / d
print ('Voce pode comprar ${:.2f}'.format(conv))