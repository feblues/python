print ('Programa de calculo de multa')
vel = float(input('Digite a velocidade ao passar pelo radar (em KM): '))
if vel > 80:
    dif = vel - 80
    multa = dif * 7
    print ('Voce passou na velocidade de {:.2f} km/h'.format(vel))
    print ('Voce ultrapassou a velocidade em {:.2f} km/h'.format(dif))
    print ('Sua multa será de R${:.2f}'.format(multa))
else:
    print ('Voce nao passou a velocidade maxima. Parabens!!!!')
