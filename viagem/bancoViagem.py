import json
import veiculo.bancoVeiculo as bcVl
baseViagem = {}


def verificaPlaca(placa):
    return(placa in bcVl.baseVeiculos)

def verificaStatus(placa):
    return('status' in baseViagem)

def serializarJson():
    with open('viagem/bancoViagem.json', 'w') as arqJson:
        json.dump(baseViagem, arqJson, indent=4)