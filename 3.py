frase = 'O Python é uma linguagem de programação '\
'multiparadigma. '\
'Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais = 0
letra_que_apareceu_mais = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais < quantas_vezes:
        qtd_apareceu_mais = quantas_vezes
        letra_que_apareceu_mais = letra_atual

    i+=1

print(f'A letra que apareceu mais vezes foi o {letra_que_apareceu_mais} que aparececu {qtd_apareceu_mais}x')