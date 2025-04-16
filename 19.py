lista = []
import os
while True:
    opcao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ')


    if opcao == 'i':
        os.system('cls')
        inserir = input('Qual item deseja inserir na lista ? ')
        lista.append(inserir)
        continue
    elif opcao == 'a' and lista == []:
        print('Não há nada para apagar, macho')
        continue
    elif opcao == 'l' and lista == []:
        print('Não há nada para listar, macho')
        continue
    elif opcao == 'a' and len(lista) > 0:
        apagar = input('Qual item você deseja apagar?')
        lista.remove(apagar)
        continue
    elif opcao == 'l' and len(lista) > 0:
        print(lista)

    sair = input('Quer sair? [n]ão [s]im')
    if sair == 's':
        break
    else:
        continue

