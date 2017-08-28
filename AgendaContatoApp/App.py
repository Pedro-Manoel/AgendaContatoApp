from model.Agenda import Agenda
import json


def agendaExistJson():
    try:
        jsonAgenda = open("agenda.json")
        json.load(jsonAgenda)
        return True
    except:
        print("ERRO!, O arquivo não foi carregado com sucesso")
        return False


def CriarAgenda():
    print("...............MENU...............")
    print("1) Criar Agenda")
    print("2) Sair")
    op = int(input(">>: "))
    if op == 1:
        nome = input("Nome: ")
        email = input("Email: ")
        nascimento = input("Nascimento: ")
        agenda = Agenda(nome, email, nascimento)
        print("Agenda criada com sucesso")
        agenda.salvarJson()
        return agenda
    if op== 2:
        exit(0)

def menuAgenda(agenda):
    print("...............MENU...............")
    print("1) Incluir Contato")
    print("2) Excluir Contato")
    print("3) Listar Contatos")
    print("4) Buscar Contato")
    print("5) Número de Contatos")
    # salvar em json
    #
    print("6) Sair")
    op = int(input(">>: "))

    if op==1:
        print("CADASTRANDO CONTATO")
        nome = input("Nome: ")
        email = input("Email: ")
        nascimento = input("Nascimento: ")
        agenda.incluirContato(nome,email,nascimento)
    if op==2:
        agenda.excluirContato()
    if op==3:
        agenda.listarContatos()
    if op==4:
        agenda.buscarContato()
    if op==5:
        print("%i Contatos"%agenda.contarContatos())
    if op==6:
        exit(0)

def carregarAgendaJson():
    try:
        jsonAgenda = open("agenda.json","r")
        jsonString = json.load(jsonAgenda)
        nome = (jsonString["agenda"]["proprietario"]["nome"])
        email = (jsonString["agenda"]["proprietario"]["email"])
        nascimento = (jsonString["agenda"]["proprietario"]["nascimento"])
        agenda = Agenda(nome,email,nascimento)
        try:
            agenda.agendaJson = jsonString
            agenda.contato = jsonString["contatos"]
            return agenda
        except:
            return agenda
    except:
        print("ERRO!, O arquivo não foi carregado com sucesso")



def main():

    continuar = True

    while(continuar):

        if agendaExistJson() == False:
            agenda = CriarAgenda()
        else:
            agenda = carregarAgendaJson()
            menuAgenda(agenda)

if __name__ == "__main__":
    main()


