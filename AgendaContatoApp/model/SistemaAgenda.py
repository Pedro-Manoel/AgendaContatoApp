from model.Agenda import Agenda
from datetime import *
from json import JSONDecodeError
import json

class SistemaAgenda:
    def agendaExistJson(self):
        try:
            jsonAgenda = open("agenda.json")
            json.load(jsonAgenda)
            return True
        except JSONDecodeError:
            return False
        except FileNotFoundError:
            arquivo = open("agenda.json","w")
            return False
        except:
            print("Erro Na Leitura Do Arquivo Json")



    def criarAgenda(self):
        print("")
        print("==================================")
        print("--------------|MENU|--------------")
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
                while (True):
                    try:
                        print("Data de Nascimento: ")
                        dia = int(input("  Dia: "))
                        mes = int(input("  Mês: "))
                        ano = int(input("  Ano: "))
                        print("")
                        agenda = Agenda(nome, email, dia, mes, ano)
                        print("Agenda Criada Com Sucesso\n")
                        agenda.salvarJson()
                        return agenda
                        break
                    except ValueError:
                        print("")
                        print("Digite Uma Data De Nascimento Válida\n")
                        continue
            elif op == 2:
                exit(0)
            else:
                print("")
                print("Digite Um Número Válido\n")
        except ValueError:
            print("")
            print("Digite Um Número Válido\n")

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
        print("5) Número De Contatos")
        print("6) Excluir Agenda")
        print("7) Sair")
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
                while(True):
                    try:
                        print("Data De Nascimento: ")
                        dia = int(input(" Dia: "))
                        mes = int(input(" Mês: "))
                        ano = int(input(" Ano: "))
                        print("")
                        agenda.incluirContato(nome, email, dia, mes, ano)
                        break
                    except:
                        print("")
                        print("Digite Uma Data De Nascimento Válida\n")
                        continue
            elif op == 2:
                if agenda.contarContatos() == 0:
                    print("Esta Agenda Não Possui Contatos Salvos")
                else:
                    nome = input("Digite O Nome Do Contato Que Dezeja Excluir: ")
                    agenda.excluirContato(nome)
            elif op == 3:
                agenda.listarContatos()
            elif op == 4:
                if agenda.contarContatos() == 0:
                    print("Esta Agenda Não Possui Contatos Salvos")
                else:
                    agenda.buscarContato()
            elif op == 5:
                print("Contatos Salvos Na Agenda: %i " % agenda.contarContatos())

            elif op ==6:
                self.excluirAgenda()

            elif op == 7:
                print("Agenda Encerrada...")
                exit(0)
            else:
                print("")
                print("Digite Um Número Válido\n")
        except ValueError:
            print("")
            print("Digite Um Número Válido\n")

    def carregarAgendaJson(self):
        try:
            jsonAgenda = open("agenda.json", "r")
            jsonString = json.load(jsonAgenda)
            nome = (jsonString["agenda"]["proprietario"]["nome"])
            email = (jsonString["agenda"]["proprietario"]["email"])
            nascimento = (jsonString["agenda"]["proprietario"]["nascimento"])
            data = datetime.strptime(nascimento,"%Y-%m-%d").date()
            agenda = Agenda(nome, email,data.day,data.month,data.year)
            try:
                agenda.agendaJson = jsonString
                agenda.contato = jsonString["contatos"]
                return agenda
            except:
                return agenda
        except:
            print("ERRO - O Arquivo Não Foi Carregado Com Sucesso")


    def excluirAgenda(self):
        while(True):
            try:
                print("Confirmar Exclusão Da Agenda")
                print("1) Excluir")
                print("2) Cancelar")
                try:
                    op = int(input(">>: "))
                    if op==1:
                        jsonAgenda = open("agenda.json", "w")
                        jsonAgenda.close()
                        print("")
                        print("Agenda Excluida Com Sucesso\n")
                        break
                    elif op==2:
                        break
                    else:
                        print("")
                        print("Digite Um Número Válido\n")
                except:
                    print("")
                    print("Digite Um Número Válido\n")
            except:
                print("")
                print("Erro Ao Excluir Agenda\n")







