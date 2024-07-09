import random


def Menu():
    while True:
        print("BEM VINDO AO JOGO DE ADIVINHAÇÃO)\n1- Começar\n2- Sair")
        escolha = int(input("\nEscolha uma das opções: "))
        if escolha == 1:
            # Jogo()
            break
        elif escolha == 2:
            break
        else:
            print("\nOpção invalida, tente novamente...")
