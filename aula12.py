nome = str(input('Qual e o seu nome? '))
if nome == 'Felipe':
    print ('Que nome bonito!')
elif nome == 'Tatiana':
    print ('So olhando o seu nome, voce deve ser brava!!!!')
elif nome in 'Ana Claudia Jessica Juliana':
    print ('Belo nome feminino')
else:
    print ('Nome normal!!!')
print ('Tenha um bom dia, {}!'.format(nome))