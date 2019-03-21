print('-'*25)
print ('Calculo IMC')
print('-'*25)
alt = float(input('Informe a altura (ex:1.77) : '))
pes = float(input('Informe o peso (ex:68.9) : '))
imc = pes / (alt**2)
if imc < 18.5:
    print('Seu IMC é {:.2f}, voce esta abaixo do seu peso.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f}, seu peso é ideal!!! PARABENS!!!'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.2f} voce esta com sobrepeso!!!!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f}, voce esta com Obesidade!!!'.format(imc))
else:
    print('Seu IMC é {:.2f}, está com obesidade morbida!!!'.format(imc))