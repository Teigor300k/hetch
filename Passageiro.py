from Usuario import Usuario

class  Passageiro(Usuario):


    def __init__(self, nome, telefone, email, idade, BI, dinheiro) -> None:
        super().__init__(nome, telefone, email, idade, BI) 
        self.dinheiro = dinheiro


        def __str__(self):
            return self.nome