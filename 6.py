numero_secreto = 42
tentativas = 0
while True:
    numero_tentado = int(input("Tente advinhar o número: "))
    tentativas += 1

    if numero_tentado == numero_secreto:
        print(f"Parabéns, você acertou o número com {tentativas} tentativas")
        break
    elif numero_tentado < numero_secreto:
        print('O número tentado é menor que o número secreto, tente novamente')
        continue
    else:
        print("O número tentado é maior que o número secreto, tente novamente")
        continue