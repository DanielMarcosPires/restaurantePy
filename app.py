from modelos.restaurante import Restaurante
restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__':
    main()