import os
os.system('cls')
lista = []
continuar = 0

# saudações e instruções iniciais
print(41 * '-')
print("Bem vindo ao programa 'lista interativa'.")
print("Começamos com uma lista vazia.")
print(41 * '-')
while continuar == 0:  # orientações de comandos
    print("O que você deseja fazer com a lista atual?")
    print("Digite [i] para inserir novos itens, ou")
    print("Digite [a] para apagar a lista/itens, ou")
    print("Digite [m] para mostrar a lista, ou")
    opcao = input("Digite [e] encerrar o programa: ")

# inserção de novos itens na lista    
    if opcao == "i":
        os.system('cls')
        novo_item = input("Qual item deseja inserir? ")
        lista.append(novo_item)
        os.system('cls')
        print(f"O item {novo_item} foi inserido com sucesso.")
        print(20 * '--')

# exclusão de itens constantes da lista
    elif opcao == "a":
        os.system('cls')
        print("Você deseja:")
        print("[1] Apagar toda a lista.")
        print("[2] Apagar um item específico.")
        opcao2 = input("Escolha: ")
        if opcao2 != '1' and opcao2 != '2':
            while opcao2 != '1' and opcao2 != '2':
                opcao2 = input("Valor inválido. Digite 1 ou 2: ")
                if opcao2 == '1':
                    opcao2 = int(1)
                    break
                elif opcao2 == '2':
                    opcao2 = int(2)
                    break
        elif opcao2 == '1':
            opcao2 = int(1)
        elif opcao2 == '2':
            opcao2 = int(2)
        if opcao2 == 1:
            os.system('cls')
            lista = []
            print(15 * '--')
            print("Toda a lista foi apagada com sucesso.")
            print(15 * '--')
        if opcao2 == 2:
            os.system('cls')
            print(15 * '-')
            print("A lista atual é:")
            ordem = 0
            for cont in range(len(lista)):
                print(ordem, "-", lista[cont])
                ordem += 1
            print(15 * '-')
            indice = int(input("Qual é o número do índice do item que você deseja excluir? "))
            if indice >= len(lista):
                print("A lista segue igual, pois o índice escolhido não existe.")
                print(20 * '-')
            else:
                excluido = lista[indice]
                lista.pop(indice)
                print(f"O item {excluido} foi excluído com sucesso.")
                print(15 * '-')

# mostrar a lista atual
    elif opcao == "m":
        if lista == []:
            os.system('cls')
            print(15 * '-')
            print("A lista está vazia")
            print(15 * '-')
        else:
            os.system('cls')
            print(15 * '-')
            print("A lista completa é:")
            ordem = 0
            for cont in range(len(lista)):
                print(ordem, "-", lista[cont])
                ordem += 1
            print(15 * '-')

# encerrar o programa            
    elif opcao == "e":
        os.system('cls')
        print(25 * '-')
        print("O programa foi encerrado.")
        print(25 * '-')
        continuar = 1

# validação de comandos
    else:
        os.system('cls')
        print(25 * '-')
        print("Insira uma opção válida: 'i', 'a', 'm' ou 'e'.")
        print(25 * '-')
