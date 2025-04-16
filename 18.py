#enumerate - enumera iteráveis(índices)

lista = ['Maria','Helena','Luiz']
lista.append('João')

lista_enumerada = tuple(enumerate(lista))
print(lista_enumerada)

for indice,nome in lista_enumerada:
    print(indice,nome)

