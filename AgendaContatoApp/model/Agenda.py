from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Telefone import Telefone
import json

class Agenda(Contato):
    def __init__(self, nome, email, nascimento):
         self.proprietario = Pessoa(nome, email, nascimento)
         self.agendaJson = {"agenda":{"proprietario":self.proprietario.__dict__}}
         self.contato = []
         if self.contato != []:
            self.salvarJson()
         super(Agenda,self).__init__("25", nome, email, nascimento)


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
        jsonAgenda = open("agenda.json","w")
        jsonStrinAgenda = self.agendaJson
        jsonStrinAgenda = json.dumps(jsonStrinAgenda)
        print(jsonStrinAgenda)
        jsonAgenda.write(jsonStrinAgenda)






    def listarContatos(self):
        cont = 0
        while (cont < self.contarContatos()):
            print(">>>>>>>>>> Contato-%s" %str(cont+1))
            print("Nome: %s" % (self.contato[cont]["contato"]["pessoa"]["nome"]))
            print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
            print("Data de Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
            cont += 1


    def incluirContato(self,nome,email,nascimento):
        pessoa = Pessoa(nome,email,nascimento)

        continuar = True
        listTelefone = []
        cont = 0

        while(continuar):
            op = int(input("Deseja cadastra um telefone:\n 1) Sim\n 2) Não\n>>: "))
            if op==1:
                cont+=1
                numero = input("numero: ")
                ddd = input("ddd: ")
                codicoPais = input("codicoPais: ")
                telefone = Telefone(numero,ddd,codicoPais)
                listTelefone.append({"telefone":telefone.__dict__})
            if op==2:
                continuar=False
                self.contato.append({"contato":{"pessoa":pessoa.__dict__,"telefones":listTelefone}})
                self.agendaJson["contatos"] = (self.contato)
                self.telefone.append(listTelefone)
                self.salvarJson()

    def excluirContato(self):
        cont = 0
        while (cont < self.contarContatos()):
            print("%s) Contato-%s (%s)" %(str(cont+1),str(cont+1),(self.contato[cont]["contato"]["pessoa"]["nome"])))
            cont += 1
            if cont == self.contarContatos():
                print("%i) Cancelar"%(cont+1))
        op = int(input(">>: "))
        if op==(cont+1):
            print("CANCELADO")
        else:
            del(self.contato[op-1])
            self.salvarJson()



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









