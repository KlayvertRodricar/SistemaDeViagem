import viagem.bancoViagem as bcVg
import veiculo.bancoVeiculo as bcVl
from datetime import date, datetime


'''

# REGRAS VIAGEM
1 - bdViagens só deverá ser acessada do arquivo controlador                                             #OK
2 - A Viagem será um dicionário com as veiculo, rota, status e data                                           #OK
3 - Status deve ser True para quando criar uma viagem que entende que inicio e False para desativar a viagem, como se o carro estivesse chegado do destino. Não pode vincular um mesmo veiculo em outra viagem se tiver uma viagem com o mesmo veículo como True                                 #OK
4 - Rota, uma string mesmo dizendo para onde ele vai.   #OK
5 - O veiculo deverá ser pego do bdVeiculo.             #OK
'''

#OK
def criarViagem():
    print("")
    print("\n{:^80}".format('Cadastrar Viagem'))
    print("{:*^80}".format(""))
    print("")

    while True:
        placa = input("Digite a placa: ")
        print("")
        if bcVg.verificaPlaca(placa):
            if bcVl.baseVeiculos[placa]['motorista'] != '':
                if bcVg.verificaStatus(placa):
                    print("Veículo indisponível para seleção pois o mesmo, no momento, está em viagem")
                    print("")
                else:
                    print("Veículo selecionado")
                    print("")
                    break
            else:
                print("Veículo sem motorista. Por favor selecione um que o tenha")
                print("")
                break
        else:
            print("")
            print("Veículo desconhecido, tente novamente")

    rota = input("Digite a rota que deseja fazer ex: Serra Talhada/Recife\n")

    viagem = {'placa': placa, 'rota': rota, 'data': f'{date.today()}', 'status': True}
    
    bcVg.baseViagem[placa] = viagem
    bcVg.serializarJson()
    print("")
#OK
def finalizarViagemPorPlaca():
    if len(bcVg.baseViagem) > 0:
        print("")
        print("\n{:^80}".format("Finalizar Viagem"))
        print("{:*^80}".format(""))
        print("")
        while True:
            placa = input("Digite a placa para buscarmos no banco de dados: ")
            print("")
            if bcVg.verificaPlaca(placa):
                print("")
                print("Placa selecionada")
                print("")
                break
            else:
                print("")
                print("Não há veículos cadastradas!")
                print("")

        while True:
            choice = input(f"Deseja finalizar a viagem com rota {bcVg.baseViagem[placa]['rota']}?[S/N]").upper()
            print("")
            if choice == "S" or choice == "SIM":    
                novoStatus = False
                bcVg.baseViagem[placa]['status'] = novoStatus
                bcVg.baseViagem[placa]['dataFinal'] = date.today()
                print("Status editado com sucesso!")
                print("")
                break

            elif choice == "N" or choice == "NAO" or choice ==  "NÃO":
                print("Operação cancelada, retornando ao menu")
                print("")
                break

            else:
                print("")
                print("Digite somente S ou N")
                print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")    
#OK
def verViagensAtivas():
    print("")
    print("\n{:^80}".format("Viagens Ativas"))
    print("{:*^80}".format(""))
    print("")
    viagens = bcVg.baseViagem
    for viagem in viagens.values():
        if viagem.get('status') == True:
            print("")
            print('{:<18}{:<25}{:<15}'.format('Placa:','Rota:', 'Data:'))

            print("{:<18}{:<25}{:<15}".format(viagem.get("placa"), viagem.get("rota"), viagem.get("data")))
            print("")
        else:
            print("")
            print("Nenhuma viagem no momento")
            print("")
#OK
def veiculosEmViagem():
    if len(bcVg.baseViagem) > 0:
        print("")
        print("\n{:^80}".format('Veículos em Viagem'))
        print("{:*^80}".format(""))
        print("")
        viagens = bcVg.baseViagem
        for viagem in viagens.values():
            if viagem.get('status') == True:
                print('{:<18}{:<25}'.format('Placa:','Rota:'))

                print("{:<18}{:<25}".format(viagem.get("placa"), viagem.get("rota")))
                print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")
#OK
def veiculosDisponiveisParaViagem():
    if len(bcVg.baseViagem) > 0:
        print("")
        print("\n{:^80}".format("Veículo Disponíveis"))
        print("{:*^80}".format(""))
        print("")
        print("{:*^80}".format("Lista de Veículos"))

        viagem = bcVg.baseViagem
        count = 1

        for viagem in bcVg.baseViagem.values():
            if viagem.get('status') == False:
                print(f"Motorista: {count}\nVeículo de placa: {viagem.get('placa')}")
                count += 1
    else:
        print("Lista vazia, adicione alguém")
#OK
def listarTodosViagens():
    if len(bcVg.baseViagem) > 0:
        print("")
        print("\n{:^80}".format("Lista Viagem"))
        print("{:*^80}".format(""))
        print("")
        viagens = bcVg.baseViagem
        for viagem in viagens.values():
            print('{:<18}{:<25}{:<25}{:<15}'.format('Placa:','Rota:', 'Status:', 'Data:'))

            print("{:<18}{:<25}{:<25}{:<15}".format(viagem.get("placa"), viagem.get("rota"),viagem.get("status"), viagem.get("data")))
            print("")
    else:
        print("Lista vazia, adicione alguém")
        print("")
#FAZER POR PERÍODO
def listarTodasViagensPorPeriodo():
    if len(bcVg.baseViagem) > 0:
        print("\n{:^80}".format("Listar por período"))
        print("{:*^80}".format(""))
        print("")
        

        print("Formato da data: ano-mês-dia")
        dataViagemInicial = input("Digite a data inicial: ")
        dataViagemFinal = input("Digite a data final: ")
        print("")


        viagens = bcVg.baseViagem
        for viagem in viagens.values():
            if viagem.get('data') >= dataViagemInicial and viagem.get('data') <= dataViagemFinal:

                print('{:<18}{:<25}{:<25}{:<15}'.format('Placa:','Rota:', 'Status:', 'Data:'))

                print("{:<18}{:<25}{:<25}{:<15}".format(viagem.get("placa"), viagem.get("rota"),viagem.get("status"), viagem.get("data")))
                print("")
        print("Verificação finalizada")
        print("")
    else:
        print("Lista vazia, adicione alguém")
#OK
def menuViagem(): 
    while True:
        print("-----------MENU VIAGEM---------\n"
        "1 - Criar Viagem\n"
        "2 - Finalizar Viagem por placa\n" #Aqui mude somente o status de True para False #OK
        "3 - Viagens Ativas\n"
        "4 - Veiculos que estão em Viagem\n"
        "5 - Veiculos que estão Disponíveis para Viagem\n"
        "6 - Listar todas as viagens\n"
        "7 - Listar todas as viagens por período\n"#- dat"inicial e final (todas as viagens deste período)
        "8 - SAIR\n"
        "-----------MENU VIAGEM---------\n")   

        choice = input("Escolha a opção do menu de viagem que você deseja: ")
        
        if choice == "1":
            criarViagem()

        elif choice == "2":
            finalizarViagemPorPlaca()

        elif choice == "3":
            verViagensAtivas()
  
        elif choice == "4":
            veiculosEmViagem()

        elif choice == "5":
            veiculosDisponiveisParaViagem()

        elif choice == "6":
            listarTodosViagens()

        elif choice == "7":
            listarTodasViagensPorPeriodo()
                                            
        elif choice == "8":
            return

        else:
            print("Digite somente uma opção válida")
            print("")