from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Telefone import Telefone
import json
from datetime import *

class Agenda(Contato):
    def __init__(self, nome, email, dia, mes, ano):
         self.proprietario = Pessoa(nome, email, dia, mes, ano)
         self.agendaJson = {"agenda":{"proprietario":self.proprietario.__dict__}}
         self.contato = []
         self.telefone = []
         if self.contato != []:
            self.salvarJson()



    def contarContatos(self):
        return len(self.contato)



    def carregarJson(self):
        try:
            jsonAgenda = open("agenda.json","r")
            self.agendaJson = json.load(jsonAgenda)
            print(self.agendaJson)
        except:
            print("ERRO!, O Arquivo Não Foi Carregado Com Sucesso")


    def salvarJson(self):
        try:
            jsonAgenda = open("agenda.json","w")
            jsonStrinAgenda = self.agendaJson
            jsonStrinAgenda = json.dumps(jsonStrinAgenda, indent=4)
            jsonAgenda.write(jsonStrinAgenda)
        except:
            print("Erro Ao Salvar No Arquivo Json")






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
            print("Esta Agenda Não Possui Contatos Salvos")


    def incluirContato(self,nome,email,dia,mes,ano):
        pessoa = Pessoa(nome,email,dia,mes,ano)

        continuar = True
        listTelefone = []
        cont = 0
        data = str(date.today())

        while(continuar):
            print("Deseja Incluir Um Telefone:")
            print("1) Sim")
            print("2) Não")
            print("")
            try:
                op = int(input(">>: "))
                if op==1:
                    cont+=1
                    numero = input("Número: ")
                    try:
                        ddd = int(input("DDD: "))
                        codicoPais = int(input("Códico Do País: "))
                        print("")
                        telefone = Telefone(numero,ddd,codicoPais)
                        listTelefone.append({"telefone":telefone.__dict__})
                        print("")
                        print("Telefone Salvo\n")
                    except ValueError:
                        print("")
                        print("Cadastro Do Telefone Cancelado...Erro Número Inválido\n")
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
                    print("Digite Um Número Válido\n")
            except ValueError:
                print("")
                print("Digite Um Número Válido\n")

    def excluirContato(self,nome):
        nome = nome.upper()
        cont = 0
        while (cont < self.contarContatos()):
            nomeBusca = str(self.contato[cont]["contato"]["pessoa"]["nome"])
            nomeBusca = nomeBusca.upper()
            if nome == nomeBusca:
                print("==================================")
                print("INFORMAÇÕES DO CONTATO ENCONTRADO")
                print("==================================")
                print("%s"%(self.contato[cont]["contato"]["pessoa"]["nome"]))
                print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
                print("Data De Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
                print("Data De Sua Criação: %s\n" % (self.contato[cont]["contato"]["criacao"]))
                print("Confirmar Exclusão: ")
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
                        print("Digite Um Número Válido\n")
                        continue
                except ValueError:
                    print("")
                    print("Digite Um Número Válido\n")
                    continue
            if (nome != (self.contato[cont]["contato"]["pessoa"]["nome"]) and cont+1 == self.contarContatos()):
                print("")
                print("Este Contato Não Existe Na Agenda\n")
                print("Deseja Tentar Novamente")
                print("1) Sim")
                print("2) Não")
                try:
                    op = int(input(">>: "))
                    if op==1:
                        print("")
                        nome = input("Digite O Nome Do Contato Que Deseja Excluir: ")
                        cont = 0
                        continue
                    elif op==2:
                        break
                    else:
                        print("Digite Um Número Válido\n")
                except ValueError:
                    print("Digite Um Número Válido\n")
                    continue
            cont += 1




    def buscarContato(self):
        nomeBusca = input("Digite O Nome Da Pessoa: ")
        nomeBusca = nomeBusca.upper()
        cont=0

        while(cont < self.contarContatos()):
            nomeContato = str(self.contato[cont]["contato"]["pessoa"]["nome"])
            nomeContato = nomeContato.upper()
            if (nomeBusca == nomeContato):
                print("==================================")
                print("INFORMAÇÕES DO CONTATO ENCONTRADO")
                print("==================================")
                print("Nome: %s"%(self.contato[cont]["contato"]["pessoa"]["nome"]))
                print("Email: %s" % (self.contato[cont]["contato"]["pessoa"]["email"]))
                print("Data De Nascimento: %s" % (self.contato[cont]["contato"]["pessoa"]["nascimento"]))
                print("Data De Sua Criação: %s" % (self.contato[cont]["contato"]["criacao"]))
                self.telefone = self.agendaJson["contatos"][cont]["contato"]["telefones"]
                self.listarTelefones()
                print("==================================")
                print("1) Buscar Novamente")
                print("2) Voltar Para O Menu")
                op = int(input(">>: "))
                if op == 1:
                    cont = 0
                    print("")
                    nomeBusca = input("Digite O Nome Da Pessoa: ")
                if op== 2:
                    break
            else:
                cont += 1
                if cont >= self.contarContatos():
                    print("")
                    print("CONTATO NÃO ENCONTRADO\n")
                    print("1) Buscar Novamente")
                    print("2) Voltar Para O Menu")
                    op = int(input(">>: "))
                    if op==1:
                        cont = 0
                        print("")
                        nomeBusca = input("Digite O Nome Da Pessoa: ")
                    if op==2:
                        break









