import os

os.system('cls')

class Carro:
    modelos = []
    def __init__(self, modelo,cor,ano):
        self.modelo = modelo,
        self.cor = cor,
        self.ano = ano,
        Carro.modelos.append(self)

    def __str__(self):
       return f'{self.modelo} | {self.cor} | {self.ano}'
    
carro1 = Carro(
    modelo="modelo 1",
    cor="Amarelo",
    ano="2003"
)

print(carro1)