from model.SistemaAgenda import SistemaAgenda

def main():

    sistema = SistemaAgenda()

    while(True):

        if sistema.agendaExistJson() == False:
            agenda = sistema.criarAgenda()
        else:
            agenda = sistema.carregarAgendaJson()
            sistema.menuAgenda(agenda)

if __name__ == "__main__":
    main()

