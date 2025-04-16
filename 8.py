senha_correta = 'python123'
tentativas = 0
while True:
    senha_tentada = input("Digite sua senha: ")
    tentativas += 1

    if senha_tentada == senha_correta and tentativas < 3:
        print('Acesso Concedido')
        break
    elif senha_tentada != senha_correta and tentativas < 3:
        continue
    elif senha_tentada != senha_correta and tentativas == 3:
        print("Acesso Negado")
        break
