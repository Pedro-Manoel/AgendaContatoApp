"""
responsável pelo controle da class Agenda
"""


# Contastes do tipo string que conterão as mensagens de erro e de informações mais comuns da aplicação.
numeroInvalido = ("\nDigite Um Número Válido ") # Erro ao digitar por exemplo uma letra onde se deve receber um número.
numeroForaDeContesto = ("\nNão Existe Esta Opção ") # Erro ao digitar um número que esteja fora das opções que se pedem.
semContatosSalvos = ("\nNão Existem Contatos Salvos Na Agenda ") # Erro ao tentar algum método que envolva manipular ou extrair informações dos contatos da agenda onde a agenda não possui nenhum contato.
contatoNaoExiste = ("\nEste Contato Não Existe Na Agenda ") # Informação dada ao buscar um contato que não existe na agenda.
dataNascimentoInvalida = ("\nDigite Uma Data De Nascimento Válida \n") # Erro ao digitar uma data de nascimento que não seja válida ou digitar algo diferente de um números.
excluirAgenda = ("\nErro Ao Excluir Agenda ") # Erro ao tentar excluir a agenda.


class Agenda():
    def __init__(self, proprietario):
         self.proprietario = proprietario
         self.contatos = []



    def contarContatos(self):
        # Retornara o número de contatos salvos atualmente na agenda.
        return (len(self.contatos))


    def listarContatos(self):
        # Mostrar as informações de cada contato salvo na agenda.
        cont = 0 # Variável usada para enumerar os contatos ao Mostra-los na tela.
        if (self.contarContatos() == 0 ): # Verificando se a agenda possui algum contato salvo se não possuir exibir a mensagem correspondente e encerrar o método.
            print(semContatosSalvos)
        else: # Confirmado a existência de contatos na agenda prosseguir com o método de listagem.
            print("==================================\n"
                  "CONTATOS SALVOS\n"
                  "==================================\n")
            for contato in self.contatos:
                cont += 1
                print("==================================")
                print("%iº-Contato" %cont) # Enumerando os contatos.
                print("Nome: %s" % (contato.pessoa.nome)) # Mostrando nome.
                print("Email: %s" % (contato.pessoa.email))# Mostrando email.
                print("Data De Nascimento: %s" % (contato.pessoa.nascimento))# Mostrando a data de nascimento.
                print("Data De Criação Do Contato: %s" % str(contato.criacao))# Mostrando a data de criação do contato.
                contato.listarTelefones()
                print("==================================")


    def incluirContato(self,contato):
        # incluindo contato na lista de contatos da agenda.
        self.contatos.append(contato)


    def excluirContato(self,nome):
        # Buscando contato pelo nome na lista de contatos da agenda e se encontrado ele será apagado da agenda.

        cont = 0 # Variável de controle para armazenar o index do contato atual.
        for contato in self.contatos: # loop Principal: Percorrendo a lista de contatos.
            busca = contato.pessoa.nome # Armazenando nome do atual contato.
            if (nome.upper() == busca.upper()):
                self.buscarContato(nome) # Chamando o buscar contato para exibir as informações do contato que deseja excluir.
                while(True): # Loop de Erro caso o usuário digite um número invalido.
                    print("\nConfirmar Exclusão:\n"
                          "1) Sim\n"
                          "2) Não")
                    try:
                        op = int(input(">>: ")) # Variável que vai armazenar o número da opção do usuário.
                        if op == 1:
                            del (self.contatos[cont]) # Deletando contato da lista atraves do index armazenado na variável cont.
                            print("\nContato Excluido\n")
                            return None# Parando loop e encerrando o método.
                        elif op == 2:
                            return None# Parando loop e encerrando o método.
                        else:
                            print(numeroForaDeContesto)
                    except ValueError:
                        print(numeroInvalido)
            cont += 1
            if cont == self.contarContatos(): # Quando chegar ao final do loop e o contato não tiver sido encontrado.
                print(contatoNaoExiste)


    def buscarContato(self,nome):
        # Buscando contato pelo seu nome dentro da lista de contatos da agenda.

        encontrado = False # Variável que vai armazenar True se o contato for encontrado ou False se não for encontrado.
        for contato in self.contatos: # Percorrendo a lista de contato.
            busca = contato.pessoa.nome # Armazenando nome do atual contato.
            if (nome.upper() == busca.upper()): # Fazendo a comparação com os dois nomes em caixa alta.
                encontrado = True
                print("\n==================================\n"
                      "INFORMAÇÕES DO CONTATO ENCONTRADO\n"
                      "==================================")
                print("%s" % (contato.pessoa.nome))
                print("Email: %s" % (contato.pessoa.email))
                print("Data De Nascimento: %s" % (contato.pessoa.nascimento))
                print("Data De Criação Do Contato: %s" % str(contato.criacao))
                contato.listarTelefones()
                break
        if encontrado == False:  # Se o contato não for encontrado.
            print(contatoNaoExiste)



