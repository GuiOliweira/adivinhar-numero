import random


def Menu():
    while True:
        print("\nBEM VINDO AO JOGO DE ADIVINHAÇÃO\n1- Começar\n2- Sair")
        escolha = int(input("\nEscolha uma das opções: "))
        if escolha == 1:
            IntroGame()
            break
        elif escolha == 2:
            break
        else:
            print("\nOpção inválida, tente novamente...")


def IntroGame():
    print("-" * 50)
    print("Olá jogador, você deve informar o número que deseja para o intervalo. Lembrando que começa do 0 e vai até o número em que você escolher...\n")
    numero_user = int(input("Digite o número de limite desejado: "))
    numero_certo = random.randint(0, numero_user)
    Jogo(numero_certo)


def Jogo(numero):
    print("\nNúmero gerado!! Vamos lá...")
    tentativas = 0
    dobro = numero * 2
    metade = numero / 2
    while True:
        tentativa_user = int(input("Tente adivinhar o número: "))
        tentativas += 1
        if tentativa_user == numero:
            print("\nPARABÉNS VOCÊ ACERTOU!!!")
            print(f"Número de tentativas: {tentativas}")
            while True:
                escolha = int(
                    input("\nDeseja voltar ao menu? (1-sim 2-nao)   :"))
                if escolha == 1:
                    Menu()
                    break
                elif escolha == 2:
                    break
                else:
                    print("\nOpção inválida, tente novamente...")
            break
        elif tentativa_user > numero:
            print("Muito alto, tente um número mais baixo...")
        elif tentativa_user < numero:
            print("Muito baixo, tente um número mais alto...")


Menu()
