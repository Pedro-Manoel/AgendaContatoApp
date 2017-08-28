from model.Telefone import Telefone
from model.Pessoa import Pessoa
import datetime

class Contato(Telefone):
    def __init__(self, criacao, nome, email, nascimento):
        self.criacao = datetime.datetime.now()
        self.pessoa = Pessoa(nome, email, nascimento)
        self.telefone = []
        super(Contato,self).__init__(0, 0, 0)

    def listarTelefones(self,numContato):
        print(self.telefone[numContato])

        cont = 0

        while(cont <len(self.telefone[numContato])):
            print(">>> Telefone-%s"%str(cont+1))
            print("Número: %s"%self.telefone[numContato][cont]["telefone"]["numero"])
            print("DDD: %i"%int(self.telefone[numContato][cont]["telefone"]["ddd"]))
            print("Códico do País: %i"%int(self.telefone[numContato][cont]["telefone"]["codicoPais"]))
            cont +=1



