from datetime import *

class Pessoa:
    def __init__(self, nome, email, dia, mes ,ano):
        self.nome = nome
        self.email = email
        self.nascimento = str(date(ano,mes,dia))


