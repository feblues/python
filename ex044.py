valor = float(input('Digite o valor do produto: R$ '))
print ('1. Pagamento a Vista')
print ('2. Pagamento no Cartao em 1 vez')
print ('3. Pagamento no Cartao em 2 vezes')
print ('4. Pagamento no Cartao em 3 vezes ou mais')
menu=int(input('Escolha a opcao: '))
if menu==1:
    preco = valor - ((valor/100)*10)
    print ('O Valor pago pelo produto será {:.2f}'.format(preco))
elif menu==2:
    preco = valor - ((valor / 100) * 5)
    print('O Valor pago pelo produto será {:.2f}'.format(preco))
elif menu==3:
    preco = valor
    print('O Valor pago pelo produto será {:.2f}'.format(preco))
elif menu==4:
    preco = valor + ((valor / 100) * 20)
    print('O Valor pago pelo produto será {:.2f}'.format(preco))