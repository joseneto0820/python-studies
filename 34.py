def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)


v= executa(saudacao, 'Bom dia')
print(v)

