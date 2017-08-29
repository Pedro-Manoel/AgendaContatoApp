from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Telefone import Telefone
import json
import datetime

class Agenda(Contato):
    def __init__(self, nome, email, nascimento):
         self.proprietario = Pessoa(nome, email, nascimento)
         self.agendaJson = {"agenda":{"proprietario":self.proprietario.__dict__}}
         self.contato = []
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
            jsonStrinAgenda = json.dumps(jsonStrinAgenda)
            jsonAgenda.write(jsonStrinAgenda)
        except:
            print("Erro ao salvar no arquivo json")






    def listarContatos(self):
        cont = 0
        while (cont < self.contarContatos()):
            print(">>>>>>>>>> Contato-%s" %str(cont+1))
            print("Nome: %s" % (self.contato[cont]["contato"]["pessoa"]["nome"]))
            print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
            print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
            print("Data de Criação: %s" % (self.contato[cont]["contato"]["criacao"]))
            self.telefone = self.agendaJson["contatos"][cont]["contato"]["telefones"]
            self.listarTelefones()
            cont += 1


    def incluirContato(self,nome,email,nascimento):
        pessoa = Pessoa(nome,email,nascimento)

        continuar = True
        listTelefone = []
        cont = 0
        data = str(datetime.datetime.now())

        while(continuar):
            print("Deseja cadastra um telefone:")
            print("1) Sim")
            print("2) Não")
            try:
                op = int(input(">>: "))
                if op==1:
                    cont+=1
                    numero = input("numero: ")
                    try:
                        ddd = int(input("ddd: "))
                        codicoPais = int(input("codicoPais: "))
                        telefone = Telefone(numero,ddd,codicoPais)
                        listTelefone.append({"telefone":telefone.__dict__})
                    except ValueError:
                        print("Cadastro cancelado...Erro número invalido")
                elif op==2:
                    continuar=False
                    self.contato.append({"contato":{"pessoa":pessoa.__dict__,"telefones":listTelefone,"criacao":data}})
                    self.agendaJson["contatos"] = (self.contato)
                    self.telefone.append(listTelefone)
                    self.salvarJson()
                else:
                    print("Digite um número válido")
            except ValueError:
                print("digite um número válido")

    def excluirContato(self,nome):
        cont = 0
        while (cont < self.contarContatos()):
            if nome == (self.contato[cont]["contato"]["pessoa"]["nome"]):
                print("%s"%(self.contato[cont]["contato"]["pessoa"]["nome"]))
                print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
                print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
                print("Confirma exclução: ")
                print("1) Sim")
                print("2) Não")
                try:
                    op = int(input(">>: "))
                    if op== 1:
                        del (self.contato[cont])
                        self.salvarJson()
                    elif op==2:
                        break
                    else:
                        print("Número inválido")
                except ValueError:
                    print("Número inválido")
            cont += 1




    def buscarContato(self):
        nomeBusca = input("Digite o nome da pessoa: ")
        cont=0
        op = 0
        while(cont < self.contarContatos()):
            nomeContato=(self.contato[cont]["contato"]["pessoa"]["nome"])
            if (nomeBusca == nomeContato):
                print("ENCONTRADO")
                print("Nome: %s"%(self.contato[cont]["contato"]["pessoa"]["nome"]))
                print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
                print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
                print("1) Buscar novamente")
                print("2) Voltar para o menu")
                op = int(input(">>: "))
                if op == 1:
                    cont = 0
                    nomeBusca = input("Digite o nome da pessoa: ")
                if op== 2:
                    break
            else:
                cont += 1
                if cont >= self.contarContatos():
                    print("NÃO ENCONTRADO")
                    print("1) Buscar novamente")
                    print("2) Voltar para o menu")
                    op = int(input(">>: "))
                    if op==1:
                        cont = 0
                        nomeBusca = input("Digite o nome da pessoa: ")
                    if op==2:
                        break








