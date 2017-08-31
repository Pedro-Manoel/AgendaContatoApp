from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Telefone import Telefone
import json
import datetime

"""
LEMBRETES

AJEITAR A FORMA DE DATA DE NASCIMENTO PARA PERGUNTAR DIA MES E ANO 


"""

class Agenda(Contato):
    def __init__(self, nome, email, nascimento):
         self.proprietario = Pessoa(nome, email, nascimento)
         self.agendaJson = {"agenda":{"proprietario":self.proprietario.__dict__}}
         self.contato = []
         #self.telefone = [] colocar isso somente se eliminar as herançãs
         if self.contato != []:
            self.salvarJson()
         super(Agenda,self).__init__(str(datetime.datetime.now()), nome, email, nascimento)


    def contarContatos(self):
        return len(self.contato)



    def carregarJson(self):
        try:
            jsonAgenda = open("agenda.json","r")
            self.agendaJson = json.load(jsonAgenda)
            print(self.agendaJson)
        except:
            print("ERRO!, O arquivo não foi carregado com sucesso")


    def salvarJson(self):
        try:
            jsonAgenda = open("agenda.json","w")
            jsonStrinAgenda = self.agendaJson
            jsonStrinAgenda = json.dumps(jsonStrinAgenda, indent=4)
            jsonAgenda.write(jsonStrinAgenda)
        except:
            print("Erro ao salvar no arquivo json")






    def listarContatos(self):
        cont = 0
        print("==================================")
        print("CONTATOS SALVOS")
        print("==================================")
        while (cont < self.contarContatos()):
            print("==================================")
            print("%sº-Contato" %str(cont+1))
            print("Nome: %s" % (self.contato[cont]["contato"]["pessoa"]["nome"]))
            print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
            print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
            print("Data de Criação: %s" % (self.contato[cont]["contato"]["criacao"]))
            self.telefone = self.agendaJson["contatos"][cont]["contato"]["telefones"]
            self.listarTelefones()
            print("==================================")
            cont += 1
        if self.contarContatos()==0:
            print("Esta agenda não possui contatos salvos")


    def incluirContato(self,nome,email,nascimento):
        pessoa = Pessoa(nome,email,nascimento)

        continuar = True
        listTelefone = []
        cont = 0
        data = str(datetime.datetime.now())

        while(continuar):
            print("Deseja incluir um telefone:")
            print("1) Sim")
            print("2) Não")
            print("")
            try:
                op = int(input(">>: "))
                if op==1:
                    cont+=1
                    numero = input("numero: ")
                    try:
                        ddd = int(input("ddd: "))
                        codicoPais = int(input("codicoPais: "))
                        print("")
                        telefone = Telefone(numero,ddd,codicoPais)
                        listTelefone.append({"telefone":telefone.__dict__})
                        print("")
                        print("Telefone Salvo\n")
                    except ValueError:
                        print("")
                        print("Cadastro do telefone cancelado...Erro número invalido\n")
                elif op==2:
                    continuar=False
                    self.contato.append({"contato":{"pessoa":pessoa.__dict__,"telefones":listTelefone,"criacao":data}})
                    self.agendaJson["contatos"] = (self.contato)
                    self.telefone.append(listTelefone)
                    print("")
                    print("Contato Salvo\n")
                    self.salvarJson()
                else:
                    print("")
                    print("Digite um número válido\n")
            except ValueError:
                print("")
                print("digite um número válido\n")

    def excluirContato(self,nome):
        cont = 0
        while (cont < self.contarContatos()):
            if nome == (self.contato[cont]["contato"]["pessoa"]["nome"]):
                print("==================================")
                print("INFORMAÇÕES DO CONTATO ENCONTRADO")
                print("==================================")
                print("%s"%(self.contato[cont]["contato"]["pessoa"]["nome"]))
                print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
                print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
                print("Data de sua Criação: %s\n" % (self.contato[cont]["contato"]["criacao"]))
                print("Confirma exclução: ")
                print("1) Sim")
                print("2) Não")
                try:
                    op = int(input(">>: "))
                    if op == 1:
                        del (self.contato[cont])
                        self.salvarJson()
                        print("")
                        print("Contato Excluido\n")
                        break
                    elif op == 2:
                        break
                    else:
                        print("")
                        print("Número inválido\n")
                        continue
                except ValueError:
                    print("")
                    print("Número inválido\n")
                    continue
            if (nome != (self.contato[cont]["contato"]["pessoa"]["nome"]) and cont+1 == self.contarContatos()):
                print("")
                print("Este contato não existe na agenda\n")
                print("Deseja tentar novamente")
                print("1) Sim")
                print("2) Não, voltar para o menu")
                try:
                    op = int(input(">>: "))
                    if op==1:
                        print("")
                        nome = input("Digite o nome do contato que dezeja excluir: ")
                        cont = 0
                        continue
                    elif op==2:
                        break
                    else:
                        print("Número inválido")
                except ValueError:
                    print("Número inválido")
                    continue
            cont += 1




    def buscarContato(self):
        nomeBusca = input("Digite o nome da pessoa: ")
        cont=0

        while(cont < self.contarContatos()):
            nomeContato=(self.contato[cont]["contato"]["pessoa"]["nome"])
            if (nomeBusca == nomeContato):
                print("==================================")
                print("INFORMAÇÕES DO CONTATO ENCONTRADO")
                print("==================================")
                print("Nome: %s"%(self.contato[cont]["contato"]["pessoa"]["nome"]))
                print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
                print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
                print("Data de sua Criação: %s" % (self.contato[cont]["contato"]["criacao"]))
                self.telefone = self.agendaJson["contatos"][cont]["contato"]["telefones"]
                self.listarTelefones()
                print("==================================")
                print("1) Buscar novamente")
                print("2) Voltar para o menu")
                op = int(input(">>: "))
                if op == 1:
                    cont = 0
                    print("")
                    nomeBusca = input("Digite o nome da pessoa: ")
                if op== 2:
                    break
            else:
                cont += 1
                if cont >= self.contarContatos():
                    print("")
                    print("CONTATO NÃO ENCONTRADO\n")
                    print("1) Buscar novamente")
                    print("2) Voltar para o menu")
                    op = int(input(">>: "))
                    if op==1:
                        cont = 0
                        print("")
                        nomeBusca = input("Digite o nome da pessoa: ")
                    if op==2:
                        break









