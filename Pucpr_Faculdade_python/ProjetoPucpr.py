# iniciando o menu principal 
while True:
    print("Menu principal")
    print("Bem-vindo ao menu!!! Escolha uma das opções")
    print("1 - Estudantes")
    print("2 - Disciplinas")
    print("3 - Professores")
    print("4 - Turmas")
    print("5 - Matriculas")
    print("0 - Sair")

    #Coletar dados do usuario

    opcao = int(input("Digite uma opção valida."))
    print(f"Você escolheu a opção{opcao}")
    if opcao >= 1 and opcao <= 5:
        print(f"Você escolheu a opção{opcao}")

            # Mostrando o menu secundario 
        print(f"Menu de operações - Opção {opcao}")
        print("1. listar")
        print("2. Criar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu anterior")

        # Coletar a opção do menu secundario 
        
        while True: 
            print("menu secundario")
            opcao_secundaria = int(input("digite uma opção válida"))
            if opcao_secundaria >= 1 and opcao_secundaria <= 4 :
                print(f"Você escolheu a opção secundaria {opcao_secundaria}.")
            elif opcao_secundaria == 5:
                print("você voltou ao menu principal")
                break
            else :
                print("A opção secundaria escolhida é invalida, por favor digite uma opção **valida**")

    elif opcao == 0 :
        print("Você pediu para sair")
        break
      
    else :
        print("Opção invalida, por favor escolha uma ooção valida.")  
        