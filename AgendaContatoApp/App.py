"""
responsável pela interação entre o usuário e a agenda através do sistema agenda. 
"""

from model.SistemaAgenda import SistemaAgenda

def main(Args = []):

    sistema = SistemaAgenda() # Criando um objeto do tipo SistemaAgenda.

    while(True): # Criando um loop infinito para o tratamento de erros.

        if sistema.agendaExistJson() == False: # Verificando se no arquivo JSON existe alguma agenda.
           sistema.criarAgenda() # Se não existir a agenda, criar uma e salvar no arquivo JSON.
        else:
            agenda = sistema.carregarAgendaJson() # Se existir a agenda no arquivo JSON, caregar o arquivo JSON e criar uma agenda a partir de seus dados.
            sistema.menuAgenda(agenda) # Chamando o menu da agenda.

if __name__ == "__main__":
    main()


