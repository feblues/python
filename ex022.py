n = str(input('Digite seu nome completo: ')).strip
print ('Analisando seu nome...')
print ('Seu nome em maiusculas é {}'.format(n.upper()))
print ('Seu nome em minusculas é {}'.format(n.lower()))
print ('Nome completo contem {} letras'.format(len(n)-n.count(' ')))
print ('Seu primeiro nome contem {} letras'.format(n.find(' ')))
#es = n.count(' ')
#ta = len(n)
#qu = ta - es
print ('Nome completo contem {} letras'.format(qu))
sp = n.split()
ta1 = len(sp[0])
print ('O primeiro nome contem {} letras'.format(ta1))
