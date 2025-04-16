string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a,b,*_, u = lista

print(a,u)
print(*lista)
print(*tupla)


for nome in lista:
    print(nome,end=' ')

#DESEMPACOTAMENTO NAS CHAMADAS DE FUNÇÕES