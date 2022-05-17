import json
import motorista.bancoMotorista as bcMt
import copy


baseVeiculos = {}


def verificaPlaca(placa):
    return(placa in baseVeiculos)



def serializarJson():
    with open('veiculo/bancoVeiculo.json', 'w') as arqJson:
        json.dump(baseVeiculos, arqJson, indent=4)



def verificaCpf(cpf):
    return(cpf in bcMt.baseMotoristas)



def verificaTipoCarteira(cpf, placa):
    veiculo = ""
    if bcMt.baseMotoristas[cpf]["tipoCarteira"] == "A":
        veiculo = "Moto"

    elif bcMt.baseMotoristas[cpf]["tipoCarteira"] == "B":
        veiculo = "Carro"

    elif bcMt.baseMotoristas[cpf]["tipoCarteira"] == "AB":
        veiculo = "Moto e carro"
    else:
        print("Incompatível")

    if baseVeiculos[placa]['tipoVeiculo'] == veiculo:
        baseVeiculos[placa]['motorista'] = bcMt.baseMotoristas[cpf]['nome']
        print("Motorista adicionado com sucesso!")
    else:
        print("Adição não foi possível devido a falta de experiência")
        



def copyDelete(placa):
    baseVeiculosCopy = copy.copy(baseVeiculos)
    for x in baseVeiculosCopy.keys():
        if x == placa:
            del baseVeiculos[placa]
