nome = 'Luiz'
nome = 'João'
noutra_variavel = nome
print(nome)
print(noutra_variavel)

lista_a = ['Luiz','Maria',1,True,1.2]
lista_b = lista_a
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)