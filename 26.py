vagas_ocupadas = []

while True:
    acao = input('\nO que você quer fazer?\n[e]stacionar [r]etirar [l]istar [s]air: ').lower()

    if acao == 'e':
        estacionar = input('Digite a placa do carro para estacionar: ').upper()
        if estacionar in vagas_ocupadas:
            print('Este carro já está estacionado!')
        else:
            vagas_ocupadas.append(estacionar)
            print(f'Carro {estacionar} estacionado com sucesso.')

    elif acao == 'r':
        retirar = input('Digite a placa do carro para retirar: ').upper()
        if retirar in vagas_ocupadas:
            vagas_ocupadas.remove(retirar)
            print(f'Carro {retirar} retirado com sucesso.')
        else:
            print('Carro não encontrado no estacionamento.')

    elif acao == 'l':
        if not vagas_ocupadas:
            print('Nenhum carro estacionado.')
        else:
            print('Carros estacionados:')
            for placa in vagas_ocupadas:
                print(f'- {placa}')

    elif acao == 's':
        print('Saindo do sistema de estacionamento. Até mais!')
        break

    else:
        print('Opção inválida. Tente novamente.')
