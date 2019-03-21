from math import radians, sin, cos, tan
an = float (input('Digite o angulo desejado: '))
sn = sin(radians(an))
cs = cos(radians(an))
tg = tan(radians(an))
print ('Para o angulo {}º o valor de seno é: {:.2f}, cosseno é: {:.2f}, e a tangente é:{:.2f}!'.format(an,sn,cs,tg))