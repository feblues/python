frase = input('Digite o texto: ')
print (frase[3])
'''len(frase)  - comprimento da frase
frase.count('o') - conta as palavras o
frase.count('o',0,13) - conta a quantidade de o que existe entre o caracter 0 ate o 13
frase.find('deo') - procura deo no texto e informa em qual posicao da memoria ele foi encontrado (se retornar -1 nao existe na string 
Curso in frase - existe a palavra curso na variavel frase - escreve true se existe e false se nao existe

transformacao

frase.replace('Python','Android') - substitui a palavra python por android * somente no visual
frase.upper() - substitui para maisculas
frase.lower() - substitui para minusculas
frase.capitalize() - substitui todas as para minuscula e deixa somente aprimeira em maiuscula
frase.title() - analisa a quantidade de palavras e faz o capitaliza nas iniciais de cada palavra

frase =    Aprenda Python  
frase.strip() remove os espacos inuteis
frase.rstrip() remove somente os espacoe inuteis do lado direito
frase.lstrip() remove somente os espacos inuteis do lado esquerdo

frase = curso em video python
frase.split() - divide aonde tem espaco - refaz os indices
'-'.join(frase) - inverso do split faz a juncao e inclui o - entre as palavras'''
