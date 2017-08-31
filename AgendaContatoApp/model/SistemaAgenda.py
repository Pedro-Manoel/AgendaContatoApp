from model.Agenda import Agenda
import json

class SistemaAgenda:
    def agendaExistJson(self):
        try:
            jsonAgenda = open("agenda.json")
            json.load(jsonAgenda)
            return True
        except:
            return False

    def criarAgenda(self):
        print("")
        print("==================================")
        print("---------------MENU---------------")
        print("1) Criar Agenda")
        print("2) Sair")
        print("==================================")
        try:
            op = int(input(">>:"))
            if op == 1:
                print("")
                print("==================================")
                print("CRIANDO AGENDA")
                print("==================================")
                nome = input("Nome: ")
                email = input("Email: ")
                nascimento = input("Nascimento: ")
                print("")
                agenda = Agenda(nome, email, nascimento)
                print("Agenda criada com sucesso\n")
                agenda.salvarJson()
                return agenda
            elif op == 2:
                exit(0)
            else:
                print("")
                print("Digite um número valido\n")
        except ValueError:
            print("")
            print("Digite um número valido\n")

    def menuAgenda(self, agenda):
        print("")
        print("==================================")
        print("----------Agenda: %s" % agenda.agendaJson["agenda"]["proprietario"]["nome"])
        print("==================================")
        print("--------------|MENU|--------------")
        print("1) Incluir Contato")
        print("2) Excluir Contato")
        print("3) Listar Contatos")
        print("4) Buscar Contato")
        print("5) Número de Contatos")
        print("6) Sair")
        print("==================================")
        try:
            op = int(input(">>: "))
            print("")

            if op == 1:
                print("==================================")
                print("CADASTRANDO CONTATO")
                print("==================================")
                nome = input("Nome: ")
                email = input("Email: ")
                nascimento = input("Nascimento: ")
                print("")
                agenda.incluirContato(nome, email, nascimento)
            elif op == 2:
                if agenda.contarContatos() == 0:
                    print("Esta agenda não possui contatos salvos")
                else:
                    nome = input("Digite o nome do contato que dezeja excluir: ")
                    agenda.excluirContato(nome)
            elif op == 3:
                agenda.listarContatos()
            elif op == 4:
                if agenda.contarContatos() == 0:
                    print("Esta agenda não possui contatos salvos")
                else:
                    agenda.buscarContato()
            elif op == 5:
                print("Contatos salvos na agenda: %i " % agenda.contarContatos())
            elif op == 6:
                print("Agenda Encerrada")
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
            print("ERRO,O arquivo não foi carregado com sucesso")
