import random


print("****************************")
print("Bem vindo ao jogo de adivinhação")
print("****************************")

numero_secreto = random.randrange(1,31)
total_de_tentativas = 3


for rodada in range(1,total_de_tentativas + 1): 
    print(F"Tentativa {rodada} de {total_de_tentativas}")
    chute = int(input("Digite um número de 1 a 30: "))
    print("Você digitou" , chute)

    if (chute < 1 or chute > 30):
        print("Você deve digitar um número de 1 a 30")
        continue

          

    if (numero_secreto == chute):
        print("Você acertou")
        break

    else:
        if(chute > numero_secreto):
            print("Você errou! Seu chute foi maior do que o número secreto.")
        elif(chute < numero_secreto):
            print("Você errou! Seu chute foi menor que o número secreto.")
    



print("Fim de jogo")
