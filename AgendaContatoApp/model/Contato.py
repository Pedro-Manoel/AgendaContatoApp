from model.Telefone import Telefone
from model.Pessoa import Pessoa
import datetime

class Contato(Telefone):
    def __init__(self, criacao, nome, email, nascimento):
        self.criacao = criacao
        self.pessoa = Pessoa(nome, email, nascimento)
        self.telefone = []
        super(Contato,self).__init__(0, 0, 0)

    def listarTelefones(self):

        cont = 0

        if (len(self.telefone)==0):
            print("Este contato não possui números de telefones")
        else:
            while(cont <len(self.telefone)):
                try:
                    print(">>> Telefone-%s"%str(cont+1))
                    print("Número: %s"%self.telefone[cont]["telefone"]["numero"])
                    print("DDD: %i"%int(self.telefone[cont]["telefone"]["ddd"]))
                    print("Códico do País: %i"%int(self.telefone[cont]["telefone"]["codicoPais"]))
                    cont +=1
                except:
                    break






