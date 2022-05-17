import motorista.bancoMotorista as bcMt

'''
# REGRAS MOTORISTAS
1 - bdMotoristas só deverá ser acessada do arquivo controlador                                          #OK

2 - Motorista será um dicionário com as chaves, cpf, nome e carteira.                                          #OK

3 - Não poderá existir mais de um motorista com o mesmo 1CPF                                                 #OK

4 - A carteira só poderá ser as seguintes strings ('A' - 'B' - 'AB')                                          #OK

'''
#OK
def cadastrarMotorista():
    print("")
    print("\n{:^80}".format("Cadastrar Motorista"))
    print("{:*^80}".format(""))
    print("")
    while True:
        cpf = input("Digite o CPF: ")
        cpfVerif = bcMt.verificaCpf(cpf)
        if cpfVerif:
            print("")
            print("Cpf já cadastrado")
            print("")
        else:
            print("")
            break

    nome = input("Digite o nome: ").title()
    while True:
        print("")
        tipoCarteira = input("Digite o tipo de carteira de motorista\n(A, B, AB): ").upper()
        if tipoCarteira == "A" or tipoCarteira == "B" or tipoCarteira == "AB":
            break
        else:
            print("")
            print("Só é permitido as carteiras A, B e AB")
            print("")

    motorista = {'cpf': cpf, 'nome': nome, 'tipoCarteira': tipoCarteira}
    bcMt.baseMotoristas[cpf] = motorista
    bcMt.serializarJson()
#OK
def inspecionarMotoristaPorCpf():
    if len(bcMt.baseMotoristas) > 0:
        while True:
            cpf = input("Digite o cpf:")
            if bcMt.verificaCpf(cpf):
                print('{:<15}{:<28}{:<28}'.format('CPF', 'Nome', 'Tipo de carteira de motorista'))
                print("{:<15}{:<28}{:<28}".format(bcMt.baseMotoristas[cpf]['cpf'],bcMt.baseMotoristas[cpf]['nome'], bcMt.baseMotoristas[cpf]['tipoCarteira'] ))
                print("")
                break
            else:
                print("Motorista desconhecido")
                print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")
#OK
def editarMotorista():
    if len(bcMt.baseMotoristas) > 0:
        print("\n{:^80}".format('Editar Motorista'))
        print("{:*^80}".format(""))

        while True:
            cpf = input("Digite o CPF: ")
            if bcMt.verificaCpf(cpf):
                for motorista in bcMt.baseMotoristas.values():
                    if motorista.get('cpf') == cpf:
                        print("CPF encontrado")
                        novoNome = input("Digite o novo nome: ").title()

                        bcMt.baseMotoristas[cpf]['nome'] = novoNome
                        print("Motorista editado com sucesso!")
                        return
            else:
                print("Motorista não existe")
            choice = int(input("Deseja tentar novamente?[1-Sim/2-Não]"))
            if choice == 1:
                editarMotorista()
            else:
                break 
    else:
        print("Lista vazia, adicione alguém")
        print("")
#OK
def removerMotorista():
    if len(bcMt.baseMotoristas) > 0:
        print("")
        print("\n{:^80}".format('Remover Motorista'))
        print("{:*^80}".format(""))
        print("")

        cpf = input("Digite o CPF: ")
        print("")
        if bcMt.verificaCpf(cpf):
            escolha = input("Realmente deseja excluir?[S/N]").upper()
            print("")
            if escolha == "S":
                bcMt.copyDelete(cpf)
                print("Motorista removido com sucesso!")
                print("")
    else:
        print("Lista vazia, adicione alguém")
        print('')
#OK
def listarMotoristaPorCarteira():
    if len(bcMt.baseMotoristas) > 0:
        print("\n{:^80}".format('Listar Motorista'))
        print("{:*^80}".format(""))
    
        buscarCarteira = input("Digite o tipo de carteira para listarmos todas elas[A, B, AB]: ").upper()
        print('{:<15}{:<28}{:<28}'.format('CPF', 'Nome', 'Tipo de carteira de motorista'))
        
        for motoristas in bcMt.baseMotoristas.values():
            if motoristas.get("tipoCarteira") == buscarCarteira:
                print('{:<15}{:<28}{:<28}'.format(motoristas.get('cpf'), motoristas.get('nome'), motoristas.get('tipoCarteira')))
                print("")
            else:
                pass
        print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")
#OK
def listarTodosMotoristas():
    if len(bcMt.baseMotoristas) > 0:
        print("")
        print("\n{:^80}".format('Listar todos os Motorista'))
        print("{:*^80}".format(""))
        print("")

        print('{:<15}{:<28}{:<28}'.format('CPF', 'Nome', 'Tipo de carteira de motorista'))
        for motoristas in bcMt.baseMotoristas.values():
            print('{:<15}{:<28}{:<28}'.format(motoristas.get('cpf'), motoristas.get('nome'), motoristas.get('tipoCarteira')))
        print("\n")
    else:
        print("Lista vazia, adicione alguém")
#OK
def menuMotorista():
    while True:
        print("-----------MENU MOTORISTAS---------\n"
        "1 - Cadastrar Motorista\n"
        "2 - Buscar Motorista por cpf\n"
        "3 - Editar Nome do Motorista\n" #antes Buscar por cpf o motorista
        "4 - Remover Motorista\n"
        "5 - Listar Todos os Motorista por tipo da carteira\n" #perguntar antes qual tipo da carteira ('A' - 'B' - 'AB')
        "6 - Listar Todos os Motorista\n"
        "7 - SAIR\n"
        "-----------MENU MOTORISTAS---------\n")


        choice = input("Escolha qual opção do menu de motoristas você deseja. ")
        if choice == "1":
            cadastrarMotorista()

        elif choice == "2":
            inspecionarMotoristaPorCpf()

        elif choice == "3":
            editarMotorista()

        elif choice == "4":
            removerMotorista()

        elif choice == "5":
            listarMotoristaPorCarteira()

        elif choice == "6":
            listarTodosMotoristas()
        
        elif choice == "7":
            break

        else:
            print("Digite somente uma opção válida")
            print("")