import veiculo.bancoVeiculo as bcVl
from motorista.bancoMotorista import baseMotoristas
'''
# REGRAS VEICULOS
1 - bdVeiculos só deverá ser acessada do arquivo controlador                                        #OK
2 - Veiculo será um dicionário com as chaves, placa, tipo e motorista:                                       #OK
3 - Não pode ter dois veiculos com a mesma placa   #OK
4 - O tipo deverá ser ('MOTO' ou 'CARRO')          #OK
5 - O motorista inicialmente deverá ser None e depois que deverá referenciar com o motorista do bdMotoristas 
                                                   #OK
'''
#Ok
def cadastrarVeiculo():
    print("")
    print("\n{:^80}".format('Cadastrar Veículo'))
    print("{:*^80}".format(""))
    print("")
    while True:
        placa = input("Digite a placa: ")
        placaVerif = bcVl.verificaPlaca(placa)
        if placaVerif:
            print("")
            print("Placa já cadastrado")
            print("")
        else:
            print("")
            break

    motorista = ""

    while True:
        print("")
        tipoVeiculo = input("Digite o tipo de veículo\n1 - Moto\n2 - Carro\n3 - Moto e carro\n")
        print("")
        if tipoVeiculo == "1":
            tipoVeiculo = "Moto"
            break
        elif tipoVeiculo == "2":
            tipoVeiculo = "Carro"
            break
        elif tipoVeiculo == "3":
            tipoVeiculo = "Moto e carro"
            break
        else:
            print("")
            print("Só é permitido carro e/ou moto")
            print("")
    print("")
    print("Cadastro realizado com sucesso!")
    print("")

    veiculo = {'placa': placa, 'motorista': motorista, 'tipoVeiculo': tipoVeiculo}
    bcVl.baseVeiculos[placa] = veiculo
    bcVl.serializarJson()
#OK
def inspecionarVeiculoPorPlaca():
    if len(bcVl.baseVeiculos) > 0:
        print("")
        print("\n{:^80}".format('Inspecionar Veículo por placa'))
        print("{:*^80}".format(""))
        print("")
    
        while True:
            print("")
            placa = input("Digite a placa:")
            print("")
            if bcVl.verificaPlaca(placa):
                print("")
                print(bcVl.baseVeiculos[placa])
                print("")
                break
            else:
                print('')
                print("Veículo desconhecido")
                print("")
    else:
        print("")
        print("Lista vazia")
        print("")
#OK
def adicionarMotoristaAoVeiculo():
    if len(bcVl.baseVeiculos) > 0:
        print("\n{:^80}".format('Adicionar Motorista'))
        print("{:*^80}".format(""))
        while True:
            print("")
            placa = input("Digite a placa: ")
            print("")

            if bcVl.verificaPlaca(placa):
                break
            else:
                print("Placa desconhecida, tente novamente")
                print("")

        while True:  
            print("")  
            cpf = input("Digite o cpf do motorista referente a vaga para verificação: ")
            print("")

            if bcVl.verificaCpf(cpf):
                #Associa o tipo de carteira(A,B,AB) a o veículo, compara e adiciona
                bcVl.verificaTipoCarteira(cpf, placa)
                #compara após associação feita
                #bcVl.comparaExperienciaEVeiculo(cpf, placa)
                break
            else:
                print("")
                print("CPF inválido")
                print("")
        print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")
#OK
def removerMotoristaDoVeiculo():
    if len(bcVl.baseVeiculos) > 0:
        print("")
        print("\n{:^80}".format('Remover Motorista'))
        print("{:*^80}".format(""))
        print("")

        placa = input("Digite a placa: ")
        print("")
        if bcVl.verificaPlaca(placa):
            for motorista in bcVl.baseVeiculos.values():
                if motorista.get('placa') == placa:
                    while True:
                        choice = input("Deseja realmente excluir?[S/N]").upper()
                        if choice == "S":
                            novoMotorista = ""
                            bcVl.baseVeiculos[placa]['motorista'] = ""
                            print("Motorista removido com sucesso!")
                            print("")
                            break
                        elif choice == "N":
                            print("Cancelando exclusão")
                            print()
                            break
                        else:
                            print("Digite somente as opções indicadas")
        else:
            print("")
            print("Placa não existe")
            print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")
#OK
def listarVeiculosComMotoristas():
    if len(bcVl.baseVeiculos) > 0:
        print("")
        print("\n{:^80}".format('Listar Veículos com motoristas'))
        print("{:*^80}".format(""))
        print("{:<15}{:<28}{:<28}".format('Placa', 'Nome', 'Tipo Veiculo'))
        print("")

        buscarMotorista = ""

        for veiculos in bcVl.baseVeiculos.values():
            if veiculos.get("motorista") != buscarMotorista:
                print("{:<15}{:<28}{:<28}".format(veiculos.get('placa'), veiculos.get('motorista'), veiculos.get('tipoVeiculo')))
                print("")
            else:
                pass
    else:
        print("Lista vazia, adicione alguém")
#OK
def listarVeiculosSemMotoristas():
    if len(bcVl.baseVeiculos) > 0:
        print("")
        print("\n{:^80}".format('Listar Veículos com motoristas'))
        print("{:*^80}".format(""))
        print("")
        buscarMotorista = ""

        print("{:<15}{:<28}".format('Placa', 'tipo Veiculo'))
        print("")
        for veiculos in bcVl.baseVeiculos.values():
            if veiculos.get('motorista') == buscarMotorista:
                print("{:<15}{:<28}".format(veiculos.get('placa'), veiculos.get('tipoVeiculo')))
                print("")
            else:
                pass
    else:
        print("Lista vazia, adicione alguém")
#OK
def removerVeiculo():
    if len(bcVl.baseVeiculos) > 0:
        print("")
        print("\n{:^80}".format('Remover Veículo'))
        print("{:*^80}".format(""))
        print("")

        placa = input("Digite a placa: ")
        print("")
        if bcVl.verificaPlaca(placa):
            escolha = input("Realmente deseja excluir?[S/N]").upper()
            print("")
            if escolha == "S":
                bcVl.copyDelete(placa)
                print("Motorista removido com sucesso!")
                print("")
    else:
        print("Lista vazia, adicione alguém")
#OK
def menuVeiculo():
    while True:
        print("-----------MENU VEÍCULO---------\n"
        "1 - Cadastrar Veiculo\n"
        "2 - Buscar Veiculo por Placa\n"
        "3 - Adicionar motorista ao veiculo\n"
        "4 - Remover motorista do veiculo\n"
        "5 - Listar veiculos com motoristas\n"
        "6 - Listar veiculos sem motoristas\n"
        "7 - Remover Veiculo\n"
        "8 - SAIR\n"
        "-----------MENU VEÍCULO---------\n")


        choice = input("Escolha qual opção do menu de motoristas você deseja. ")
        if choice == "1":
            cadastrarVeiculo()

        elif choice == "2":
            inspecionarVeiculoPorPlaca()

        elif choice == "3":
            adicionarMotoristaAoVeiculo()

        elif choice == "4":
            removerMotoristaDoVeiculo()

        elif choice == "5":
            listarVeiculosComMotoristas()

        elif choice == "6":
            listarVeiculosSemMotoristas()

        elif choice == "7":
            removerVeiculo()
        
        elif choice == "8":
            break
        else:
            print("Digite somente uma opção válida")
            print("")