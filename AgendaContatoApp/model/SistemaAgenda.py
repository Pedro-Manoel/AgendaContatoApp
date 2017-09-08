"""
responsável pelo controle do menu da agenda, bem como a execução
dos metodos da agenda e da criação dos objetos, e tambem por salvar e extrair os dados
do Json

A class SistemaAgenda vai ser o canal que liga o usuário a agenda


                                    
                                                 |-- Telefone
                                                 |N
                                                 |
 Usuário => App => SistemaAgenda => Agenda => Contato
                                                 |
                                                 |1
                                                 |-- Pessoa
                                    
"""

from model.Agenda import * # o asterisco representa que alem de estar importando a classe Agenda, tambem esta importando as contantes de erro
from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Telefone import Telefone
from datetime import *
from json import JSONDecodeError
import json

class SistemaAgenda:

    def criarPessoa(self):
        #Criando e retornando o objeto Pessoa
        nome = input("Nome: ")
        email = input("Email: ")
        while (True):
            try:
                print("Data De Nascimento: ")
                dia = int(input("  Dia: "))
                mes = int(input("  Mês: "))
                ano = int(input("  Ano: "))
                nascimento = date(ano,mes,dia)
                pessoa = Pessoa(nome, email, nascimento)
                return pessoa
            except ValueError:
                print(dataNascimentoInvalida)




    def criarTelefone(self):
        # Criando e retornando o objeto Telefone
        numero = input("Número: ")  # Fora do try pois esta variável recebe um tipo string, portando independente do que for digitado não acusara erro
        try:  # Responsável pela verificação do erro de número inválido para ddd ou codicoPais
            ddd = int(input("DDD: "))
            codicoPais = int(input("Código Do País: "))
            telefone = Telefone(numero, ddd, codicoPais)
            print("Telefone Salvo\n")
            return telefone
        except ValueError:
            print(numeroInvalido)



    def criarContato(self):
        # Criando e retornando o objeto Contato
        pessoa = self.criarPessoa()
        criacao = date.today()
        contato = Contato(pessoa,criacao)

        while(True): # Criando um loop infinito para adicionar os telefones do contato
            print("\nDeseja Incluir Um Telefone:\n"
                  "1) Sim\n"
                  "2) Não\n")
            try:
                op = int(input(">>: "))  # Variável que vai armazenar o número da opção do usuário
                if op == 1:
                    telefone = self.criarTelefone()
                    contato.telefones.append(telefone)
                elif op == 2:
                    return contato
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)


    def criarAgenda(self):
        # Criando e retornando o objeto Agenda

        print("\n==================================\n"
              "--------------|MENU|--------------\n"
              "1) Criar Agenda\n"
              "2) Sair\n"
              "==================================")
        try:
            op = int(input(">>:"))
            if op == 1:
                print("==================================\n"
                      "CRIANDO AGENDA\n"
                      "==================================")
                proprietario = self.criarPessoa()
                agenda = Agenda(proprietario)
                self.salvarJson(agenda)
            elif op == 2:
                print("Agenda Encerrada...")
                exit(0)
            else:
                print(numeroForaDeContesto)
        except ValueError:
            print(numeroInvalido)

    def menuAgenda(self, agenda):
        print("\n==================================")
        print("Agenda De %s" % agenda.proprietario.nome)# Mostrando o nome do proprietário da agenda
        print("==================================\n"
              "--------------|MENU|--------------\n"
             "1) Incluir Contato\n"
             "2) Excluir Contato\n"
             "3) Listar Contatos\n"
             "4) Buscar Contato\n"
             "5) Número De Contatos\n"
             "6) Excluir Agenda\n"
             "7) Sair\n"
              "==================================")
        try:
            op = int(input(">>: ")) # Variável que vai armazenar a opção do usuário

            if op == 1:
                print("==================================\n"
                      "CADASTRANDO CONTATO\n"
                      "==================================\n")
                contato = self.criarContato()# Criando contato
                agenda.incluirContato(contato) # Adicionando o contato a agenda
                self.salvarJson(agenda) # Salvando a atualização da agenda no arquivo json
            elif op == 2:
                if agenda.contarContatos() == 0: # Verificando se a agenda possui algum contato salvo
                    print(semContatosSalvos)
                else:
                    nome = input("Nome Do Contato Que Deseja Excluir: ")
                    agenda.excluirContato(nome) # Excluindo contato, caso ele exista
                    self.salvarJson(agenda) # Salvando a atualização da agenda no arquivo json
            elif op == 3:
                agenda.listarContatos()
            elif op == 4:
                if agenda.contarContatos() == 0: # Vefiricando se a agenda possui algum contato salvo
                    print(semContatosSalvos)
                else:
                    nome = input("Nome Do Contato Que Deseja Buscar: ")
                    agenda.buscarContato(nome) # Buscando o contato na agenda pelo seu nome, caso ele exista
            elif op == 5:
                print("\nContatos Salvos Na Agenda: %i " % agenda.contarContatos())

            elif op ==6:
                self.excluirAgenda() # Excluindo a agenda atual

            elif op == 7:
                print("Agenda Encerrada...")
                exit(0) # Encerrando a aplicação
            else:
                print(numeroForaDeContesto)
        except ValueError:
            print(numeroInvalido)


    def agendaExistJson(self):
        """
        Este método vai verificar primeiramente se existe algum arquivo na pasta da
        aplicação com o nome < agenda.json >, se não existe ele vai criar o arquivo vazio
        se o arquivo existir o método vai verificar se existe alguma coisa escrita nele
        se existir ele vai retorna True senão ele vai retornar False
        """

        try:
            jsonAgenda = open("agenda.json") # Carregando arquivo json
            json.load(jsonAgenda) # Se ocorrer um erro na leitura do arquivo quer dizer que este está vazio ou com alguma coisa escrito nele que não é reconhecido como json
            return True # Caso não ocoora erro retornara True
        except JSONDecodeError:
            return False # Caso ocorra um erro na leitura do arquivo retornara False
        except FileNotFoundError: # Se não existir o arquivo
            arquivo = open("agenda.json","w") # Criando um arquivo vazio
            return False # Retornara False pois o arquivo criado esta vazio
        except: # Se ocorrer algum erro diferente dos tratados neste método
            print("Erro Na Leitura Do Arquivo Json")

    def transformEmJson(self,obj): # Responsavel por transformar os objetos em json
        if getattr(obj, "__dict__", None): # Se o objeto disponibilizar a sua formatação em dicionário
            return obj.__dict__ # Retornando o objeto em forma de dicionário

        elif type(obj) == datetime: # Se o objeto for do tipo datetime
            return obj.isoformat() # Retornara o tipo datetime como string

        else: # Caso o objeto não tenha a formatação de dicionário disponivel e não seja do tipo datetime
            return str(obj) # Retornara o str do objeto

    def salvarJson(self,agenda):
        try:
            arquivoJson = open("agenda.json","w") # Abrindo o arquivo < agenda.json > na forma de escrita
            jsonAgenda = (json.dumps(agenda, default=self.transformEmJson, indent=4)) # Transformando o objeto agenda e seus componentes em uma string json
            arquivoJson.write(jsonAgenda) # Excrevendo no arquivo
            arquivoJson.close() # Fechando arquivo < agenda.json >
        except:
            print("Erro Ao Salvar No Arquivo Json")

    def carregarAgendaJson(self):
        try:
            arquivoJson = open("agenda.json","r") # Abrindo o arquivo na forma de leitura
            agendaJson = json.load(arquivoJson) # Transformando o arquivo em um objeto do tipo dicionário
            arquivoJson.close() # Fechando o arquivo < agenda.json >

            #Criando Agenda
            nome = agendaJson["proprietario"]["nome"]
            email = agendaJson["proprietario"]["email"]
            nascimento = agendaJson["proprietario"]["nascimento"]
            proprietario = Pessoa(nome,email,nascimento)
            agenda = Agenda(proprietario)

            #Colocando os contatos e os telefones na agenda
            while(True):
                contatos = [] # Variável que vai armazenar a lista de contatos da agenda
                contatoAgenda = None # Variável que vai armazenar os contatos um por um antes de adicionar na lista de contatos
                numContatos = len(agendaJson["contatos"]) # Capturando o número de contatos da agenda para rodar o loop de preenchimento do contato
                for contato in range(numContatos):
                    numTelefones = len(agendaJson["contatos"][contato]["telefones"]) # Capturando o número de telefones do contato atual para rodar o loop de preenchimento de telefone
                    #Criando pessoa
                    nome = agendaJson["contatos"][contato]["pessoa"]["nome"]
                    email = agendaJson["contatos"][contato]["pessoa"]["email"]
                    nascimento = agendaJson["contatos"][contato]["pessoa"]["nascimento"]
                    pessoa = Pessoa(nome,email,nascimento)
                    criacao = agendaJson["contatos"][contato]["criacao"]
                    contatoAgenda = Contato(pessoa,criacao)
                    #Adicionando os telefones da pessoa
                    for telefone in range(numTelefones):
                        numero = agendaJson["contatos"][contato]["telefones"][telefone]["numero"]
                        ddd = agendaJson["contatos"][contato]["telefones"][telefone]["ddd"]
                        codicoPais = agendaJson["contatos"][contato]["telefones"][telefone]["codicoPais"]
                        telefoneContato = Telefone(numero,ddd,codicoPais)
                        contatoAgenda.telefones.append(telefoneContato) # Adicionando o telefone a lista de telefones do contato
                    contatos.append(contatoAgenda) # Adicionando o contato a lista de contatos da agenda
                agenda.contatos = contatos
                break # Parando o loop apos o preenchimento de toda a agenda

            return agenda # Retornando a agenda preenchida com os dados do json
        except:
            print("ERRO - O Arquivo Não Foi Carregado Com Sucesso")


    def excluirAgenda(self):
        while(True):
            try:
                print("\nConfirmar Exclusão Da Agenda\n"
                      "1) Excluir\n"
                      "2) Cancelar")
                try:
                    op = int(input(">>: ")) # Variável que vai armazenar a opção do usuário
                    if op==1:
                        jsonAgenda = open("agenda.json", "w") # Abrindo o arquivo < agenda.json >
                        jsonAgenda.close()# Fechando o arquivo < agenda.json >
                        print("\nAgenda Excluida Com Sucesso")
                        break
                    elif op==2:
                        break
                    else:
                        print(numeroForaDeContesto)
                except:
                    print(numeroInvalido)
            except:
                print(excluirAgenda)
