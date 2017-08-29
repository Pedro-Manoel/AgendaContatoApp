from model.Agenda import Agenda
import json

class SistemaAgenda:
    def __init__(self):
        pass


    def agendaExistJson(self):
        try:
            jsonAgenda = open("agenda.json")
            json.load(jsonAgenda)
            return True
        except:
            #print("ERRO!, O arquivo não foi carregado com sucesso")
            return False

    def criarAgenda(self):
        print("...............MENU...............")
        print("1) Criar Agenda")
        print("2) Sair")
        try:
            op = int(input(">>: "))
            if op == 1:
                nome = input("Nome: ")
                email = input("Email: ")
                nascimento = input("Nascimento: ")
                agenda = Agenda(nome, email, nascimento)
                print("Agenda criada com sucesso")
                agenda.salvarJson()
                return agenda
            elif op == 2:
                exit(0)
            else:
                print("Digite um número valido")
        except ValueError:
            print("Digite um número valido")

    def menuAgenda(self,agenda):
        print("...............Agenda: %s........."%agenda.agendaJson["agenda"]["proprietario"]["nome"])
        print("...............MENU...............")
        print("1) Incluir Contato")
        print("2) Excluir Contato")
        print("3) Listar Contatos")
        print("4) Buscar Contato")
        print("5) Número de Contatos")
        print("6) Sair")
        try:
            op = int(input(">>: "))

            if op == 1:
                print("CADASTRANDO CONTATO")
                nome = input("Nome: ")
                email = input("Email: ")
                nascimento = input("Nascimento: ")
                agenda.incluirContato(nome, email, nascimento)
            elif op == 2:
                nome = input("Digite o nome do contato que dezeja excluir: ")
                agenda.excluirContato(nome)
            elif op == 3:
                agenda.listarContatos()
            elif op == 4:
                agenda.buscarContato()
            elif op == 5:
                print("%i Contatos" % agenda.contarContatos())
            elif op == 6:
                exit(0)
            else:
                print("Digite um número válido")
        except ValueError:
            print("Digite um número válido")

    def carregarAgendaJson(self):
        try:
            jsonAgenda = open("agenda.json", "r")
            jsonString = json.load(jsonAgenda)
            nome = (jsonString["agenda"]["proprietario"]["nome"])
            email = (jsonString["agenda"]["proprietario"]["email"])
            nascimento = (jsonString["agenda"]["proprietario"]["nascimento"])
            agenda = Agenda(nome, email, nascimento)
            try:
                agenda.agendaJson = jsonString
                agenda.contato = jsonString["contatos"]
                return agenda
            except:
                return agenda
        except:
            print("ERRO!, O arquivo não foi carregado com sucesso")

