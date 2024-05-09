import funcoes

funcoes.criar_tcarros()

while True:

    escolha = funcoes.menu()

    match (escolha):

        case 1:
            funcoes.limpar_tela()
            funcoes.add_info_tcarros()

            voltar_menu = funcoes.retornar_menu()

            print(voltar_menu)

            if voltar_menu == 2:

                break
        
        case 2:
            funcoes.limpar_tela()
            funcoes.listar_carros()

            voltar_menu = funcoes.retornar_menu()

            if voltar_menu == 2:

                break

        case 3:
            funcoes.limpar_tela()
            funcoes.buscando_carro()

            voltar_menu = funcoes.retornar_menu()

            if voltar_menu == 2:

                break

        case 0:
            break