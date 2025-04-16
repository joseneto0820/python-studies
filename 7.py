numero_secreto = 13
tentativas = 0

while tentativas < 5:
    numero_tentado = int(input("Tente adivinhar o número: "))
    tentativas += 1

    if numero_tentado == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif numero_tentado < numero_secreto:
        print('O número é menor que o número secreto.')
    else:
        print('O número é maior que o número secreto.')

if tentativas == 5 and numero_tentado != numero_secreto:
    print("Você não conseguiu adivinhar o número. O número secreto era", numero_secreto)

