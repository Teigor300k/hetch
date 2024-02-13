

class Usuario(object):


    def __init__(self, nome, telefone, email, idade, BI) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.idade = idade
        self.BI = BI

    def __str__(self):
        return self.nome
        


    def comprimentar(self):
        print(f'Bom dia {self.nome}')









