import json
import copy

#baseDados nome, cpf, carteiraMotorista
#{'CPF':{nome, carteiraMotorista}}
baseMotoristas = {}

def copyDelete(cpf):
    baseMotoristasCopy = copy.copy(baseMotoristas)
    for x in baseMotoristasCopy.keys():
        if x == cpf:
            del baseMotoristas[cpf]


def verificaCpf(cpf):
    return(cpf in baseMotoristas)

def serializarJson():
    with open('motorista/bancoMotoristas.json', 'w') as arqJson:
        json.dump(baseMotoristas, arqJson, indent=4)