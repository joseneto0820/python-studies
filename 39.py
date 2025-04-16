# SISTEMA DE LOGIN

senha_correta = 'python123'
tentativas = 0
max_tentativas = 3

def verificar_senha():
    senha_digitada = input("Qual a senha dessa budega? ")
    return senha_digitada == senha_correta

while tentativas < max_tentativas:
    if verificar_senha():
        print('ACESSO LIBERADO')
        break
    else:
        tentativas += 1
        print('Senha incorreta. Tente novamente.')

if tentativas == max_tentativas:
    print('ERRO: VOCÊ CHEGOU NO MÁXIMO DE TENTATIVAS')