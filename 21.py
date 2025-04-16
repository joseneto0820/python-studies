frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')

lista_palavras_fixed = []
for i,frase in enumerate(lista_palavras):
    lista_palavras_fixed.append(lista_palavras[i].strip())


frases_unidas = ', '.join(lista_palavras_fixed)
print(frases_unidas)