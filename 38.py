lista = []

while True:
    acao = input('Escolha uma ação:\n[i]nserir [a]pagar [l]istar [s]air ')

    def inserir_item():
        item = input('Qual item deseja inserir? ')
        return lista.append(item)
    def apagar_item():
        item = input('Qual item deseja apagar? ')
        if item in lista:
            lista.remove(item)
        else:
            print('Item não encontrado')
    def listar_itens():
        if len(lista)>0:
            print(lista)
        return print('Não há itens para listar')
    def sair():
        return print('Saindo do programa')
    
    if acao == 'i':
        inserir_item()
    elif acao == 'a':
        apagar_item()
    elif acao == 'l':
        listar_itens()
    elif acao == 's':
        sair()
        break
    else:
        print('Opção Inválida.')