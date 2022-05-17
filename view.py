import motorista.controllerMotorista as ctlM
import veiculo.controllerVeiculo as ctlV
import viagem.controllerViagem as ctlVg



def menus():
    while True:
        choice = input("-----------MENU---------\n"
        "1 - Menu de Motorista\n"
        "2 - Menu de Veiculo\n"
        "3 - Menu de Viagem\n"
        "4 - SAIR\n"
        "-----------MENU---------\n")
        if choice == "1":
            ctlM.menuMotorista()
        elif choice == "2":
            ctlV.menuVeiculo()
        elif choice == "3":
            ctlVg.menuViagem()
        elif choice == "4":
            exit(0)
        else:
            print("")
            print("Escreva somente as opções do menu!")
            print("")

menus()