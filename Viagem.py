from Motorista import Motorista
from Passageiro import Passageiro

class Viagem(object):
    def __init__(self) -> None:
        self.motorista = Motorista('João Agosto', '993000123', 'joaoagosto@gmail.com', 35, '982692LA53', ('Toyota', 'azul', 'Rabo de Pato', 'LA4790'))

        self.passageiro = Passageiro('Alice Filipe', '923234432' ,'alicefilipe@gmail.com', 29,  '182692LA33', 2000.00)


    def entrar_no_carro(self):
        self.motorista.comprimentar() 
        self.motorista.detalhes_do_carro()
        self.passageiro.comprimentar()


    def total_km(self, km):
        conta = 20 * km
        return conta


    def total_pagar(self):
        conta_da_corrida = self.total_km(2) * 10
        pago = self.passageiro.dinheiro - conta_da_corrida
        print(f'Total pago pela corrida {pago}')








if __name__ == "__main__":
    viagem = Viagem()     
    viagem.entrar_no_carro()
    viagem.total_pagar()