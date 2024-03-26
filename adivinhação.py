print("****************************")
print("Bem vindo ao jogo de adivinhação")
print("****************************")

numero_secreto = 28
total_de_tentativas = 3
rodada = 1


while (rodada <= total_de_tentativas): 
    print(F"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = int(input("Digite o seu numero: "))
    print("Você digitou" , chute_str)
          

    if (numero_secreto == chute_str):
        print("Você acertou")

    else:
        if(chute_str > numero_secreto):
            print("Você errou! Seu chute foi maior do que o número secreto.")
        elif(chute_str < numero_secreto):
            print("Você errou! Seu chute foi menor que o número secreto.")
    

    rodada = rodada + 1
        


print("Fim de jogo")
