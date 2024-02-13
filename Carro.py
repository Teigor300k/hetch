class Carro(object):

    
    def __init__(self, marca, cor, modelo, matricula) -> None:
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.matricula = matricula


    def __str__(self):
        return self.matricula


    def km_percorrido(self):
        pass
