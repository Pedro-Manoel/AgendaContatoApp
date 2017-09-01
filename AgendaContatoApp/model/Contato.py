from model.Pessoa import Pessoa
from datetime import *

class Contato():
    def __init__(self, nome, email, dia, mes ,ano):
        self.criacao = date.today()
        self.pessoa = Pessoa(nome, email, dia, mes, ano)



    def listarTelefones(self):

        cont = 0

        if (len(self.telefone)==0):
            print("Este Contato Não Possui Números De Telefones\n")
        else:
            print("=====TELEFONES")
            while(cont <len(self.telefone)):
                num = self.telefone[cont]["telefone"]["numero"]
                ddd = self.telefone[cont]["telefone"]["ddd"]
                codicoPais = self.telefone[cont]["telefone"]["codicoPais"]
                try:
                    print("%sº-Telefone" % str(cont + 1))
                    print("+%i %i-%s\n"%(codicoPais,ddd,num))
                    cont +=1
                except:
                    break






