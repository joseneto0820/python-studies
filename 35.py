def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


s1 = criar_saudacao('Bom dia', 'Luiz')

print(s1())
