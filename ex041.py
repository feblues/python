from datetime import date
print('-'*25)
print('Calculo da categoria')
print('-'*25)
ano_ida = int(input('Digite o ano de nascimento: '))
ano_atu = date.today().year
id = ano_atu - ano_ida
if id <= 9:
    print('Atleta tem {} anos ---- CATEGORIA MIRIM'.format(id))
elif id > 9 and id < 15:
    print('Atleta tem {} anos ---- CATEGORIA INFANTIL'.format(id))
elif id > 14 and id < 20:
    print('Atleta tem {} anos ---- CATEGORIA JUNIOR'.format(id))
elif id > 19 and id < 21:
    print('Atleta tem {} anos ---- CATEGORIA SENIOR'.format(id))
else:
    print('Atleta tem {} anos ---- CATEGORIA MASTER'.format(id))