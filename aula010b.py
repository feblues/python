n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 8.5:
    print('Sua média foi excelente! Parabens!')
if m >= 7 and m < 8.5:
    print('Sua média foi boa! Pode melhorar!')
elif m >= 6 and m < 7:
    print('Voce passou, mas estude mais!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')