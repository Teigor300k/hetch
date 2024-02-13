from Usuario import Usuario
from Carro import Carro

class Motorista(Usuario):


    def __init__(self, nome, telefone, email, idade, BI, carro:Carro) -> None:
        super().__init__(nome, telefone, email, idade, BI) 
        self.carro = carro



    def __str__(self):
        return self.nome
    


    def detalhes_do_carro(self):
        print(f'Dados do carro {self.carro}')


  