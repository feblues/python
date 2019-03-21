print ('Calculo de passagem de onibus')
km = int(input('Digite a quilometragem a ser percorrida '))
if km > 200:
    print ('Voce pagara R${:.2f} por {} kilometros'.format(km * 0.45, km))
else:
    print('Voce pagara R${:.2f} por {} kilometros'.format(km * 0.50, km))