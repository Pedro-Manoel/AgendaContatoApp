"""
responsável pelo controle da class Contato
"""

class Contato:
    def __init__(self, pessoa, criacao = None):
        self.criacao = criacao
        self.pessoa = pessoa
        self.telefones = []

    def listarTelefones(self):
        cont = 0 # Váriavel usada para enumerar os telefones ao emprimir eles na tela
        if len(self.telefones) == 0: # Verificando se a telefones salvos no contato se não tiver ixibir a mensagem
            print("Este Contato Não Possui Telefones Salvos")
        else: # Confirmado a exitencia de telefones no contato proseguir com o metodo de listagem
            print("=====TELEFONES")
            for telefone in self.telefones:
                cont += 1
                print("%iº-Telefone" %cont)
                print("+%i %i-%s\n" %(telefone.codicoPais, telefone.ddd, telefone.numero))

