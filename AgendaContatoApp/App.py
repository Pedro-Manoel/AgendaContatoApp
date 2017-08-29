from model.SistemaAgenda import SistemaAgenda

def main():

    continuar = True
    sistema = SistemaAgenda()

    while(continuar):

        if sistema.agendaExistJson() == False:
            agenda = sistema.criarAgenda()
        else:
            agenda = sistema.carregarAgendaJson()
            sistema.menuAgenda(agenda)

if __name__ == "__main__":
    main()

