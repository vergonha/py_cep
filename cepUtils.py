import requests
import json

class Cep():
    def __init__(self, cep, ddd, rua, complemento, bairro, cidade, uf):
        self.cep=cep
        self.ddd=ddd
        self.rua=rua
        self.complemento=complemento
        self.bairro=bairro
        self.cidade=cidade
        self.uf=uf


def findCep(cep):
    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    request = json.loads(request.content)

    cep = request['cep']
    ddd = request['ddd']
    rua = request['logradouro']
    complemento = request['complemento']
    bairro = request['bairro']
    cidade = request['localidade']
    uf = request['uf']

    cep = Cep(cep, ddd, rua, complemento, bairro, cidade, uf)
    return cep

