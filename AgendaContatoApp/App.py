"""
responsável pela interação entre o usuário e a agenda 
"""

from model.SistemaAgenda import SistemaAgenda

def main():

    sistema = SistemaAgenda() # Criando um objeto do tipo sistema agenda

    while(True): # Criando um loop infinito para o menu da agenda

        if sistema.agendaExistJson() == False: # Verificando se no arquivo json existe a agenda
           sistema.criarAgenda() # Se não existir a agenda, criar uma
        else:
            agenda = sistema.carregarAgendaJson() # Se existir a agenda no arquivo json, caregar o arquivo json e criar uma agenda a partir de seus dados
            sistema.menuAgenda(agenda) # Chamando o menu da agenda

if __name__ == "__main__":
    main()

