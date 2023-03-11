import random

print("*"*37)
print("Bem-vindo ao Jogo de Adivinhação!")
print("*"*37)

numero_secreto = random.randrange(1,101)
numero_tentativas = 0
rodada = 1

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Escolhe o nível de dificuldade: "))

if nivel == 1:
    numero_tentativas = 10
elif nivel == 2:
    numero_tentativas = 5
elif nivel == 3:
    numero_tentativas = 3

for rodada in range(1, numero_tentativas + 1):
    print(f"Tentativa {rodada} de {numero_tentativas}")

    chute = int(input("Digite um número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! O número secreto é menor.")
            if rodada == numero_tentativas:
                print("O número secreto era {}.".format(numero_secreto))
        elif menor:
            print("Você errou! O número secreto é maior.")
            if rodada == numero_tentativas:
                print("O número secreto era {}.".format(numero_secreto))