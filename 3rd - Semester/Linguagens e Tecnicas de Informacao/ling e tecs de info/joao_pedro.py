from abc import ABC, abstractmethod

class Eletrodosmestico(ABC):
    def __init__(self,marca, preco, quantidade_estoque, vida_util):
        self.marca = marca
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.vida_util = vida_util

    def get_marca(self):
        return self.marca
    def set_marca(self, novo_marca):
        self.marca = novo_marca

    def get_preco(self):
        return self.preco
    def set_preco(self, novo_preco):
        self.preco = novo_preco

    def get_quantidade_estoque(self):
        return self.quantidade_estoque
    def set_quantidade_estoque(self, novo_quantidade_estoque):
        self.quantidade_estoque = novo_quantidade_estoque

    def get_vida_util(self):
        return self.vida_util
    def set_vida_util(self, novo_vida_util):
        self.vida_util = novo_vida_util

    @abstractmethod
    def ligar(self):
        pass

class Ventilador(Eletrodosmestico):
    def __init__(self, marca, preco, quantidade_estoque, vida_util, velocidade_rotacao_maxima, angulo_rotacao):
        super().__init__(marca, preco, quantidade_estoque, vida_util)
        self.velocidade_rotacao_maxima = velocidade_rotacao_maxima
        self.angulo_rotacao = angulo_rotacao

    def get_velocidade_rotacao_maxima(self):
        return self.velocidade_rotacao_maxima
    def set_velocidade_rotacao_maxima(self, novo_velocidade_rotacao_maxima):
        self.velocidade_rotacao_maxima = novo_velocidade_rotacao_maxima

    def get_angulo_rotacao(self):
        return self.angulo_rotacao
    def set_angulo_rotacao(self, novo_angulo_rotacao):
        self.angulo_rotacao = novo_angulo_rotacao

    def __str__(self):
        return f'Marca: {self.marca}\n Preco: {self.preco} reais\n Quantidade em estoque: {self.quantidade_estoque},\n ' \
               f'A vida util: {self.vida_util}\n ' \
               f'Velocidade de rotacao maxima da helice: {self.velocidade_rotacao_maxima} rotacoes por segundo,\n ' \
               f'O angulo de rotacao: {self.angulo_rotacao} graus\n'

    def ligar(self, marca):
        x = int(input('Deseja ligar ou desligar o ventilador? (1 - ligar, 0 - desligar)\n'))
        if x == 1:
            print(f'O ventilador da marca {self.marca} esta ligado\n')
            return 0
        else:
            print(f'O ventilador da marca {self.marca} esta desligado\n')
            return 0

class Microondas(Eletrodosmestico):
    def __init__(self, marca, preco, quantidade_estoque, vida_util, tempo_preparo):
        super().__init__(marca, preco, quantidade_estoque, vida_util)
        self.tempo_preparo = tempo_preparo

    def get_tempo_preparo(self):
        return self.tempo_preparo
    def set_tempo_preparo(self, novo_tempo_preparo):
        self.tempo_preparo = novo_tempo_preparo

    def __str__(self):
        return f'Marca: {self.marca}\n Preco: {self.preco} reais\n Quantidade em estoque: {self.quantidade_estoque},\n ' \
               f'A vida util: {self.vida_util}\n O tempo atual tempo de preparo: {self.tempo_preparo} segundos\n'

    def ligar(self, marca):
        x = int(input('Deseja ligar ou desligar o microondas? (1 - ligar, 0 - desligar)\n'))
        if x == 1:
            print(f'O microondas da marca {self.marca} esta ligado\n')
            return 0
        else:
            print(f'O microondas da marca {self.marca} esta desligado\n')
            return 0

    def trocar_modos(self, tempo_preparo):
        opcao = int(input('Qual modo deseja utilizar\n 1 - Pipoca\n 2 - Brigadeiro\n 3 - Arroz\n'))
        if opcao == 1:
            self.tempo_preparo = 240
            print(f'O seu prato estara pronto em {self.tempo_preparo} segundos')
            return 0
        elif opcao == 2:
            self.tempo_preparo = 360
            print(f'O seu prato estara pronto em {self.tempo_preparo} segundos')
            return 0
        else:
            self.tempo_preparo = 700
            print(f'O seu prato estara pronto em {self.tempo_preparo} segundos')
            return 0

if __name__ == '__main__':
    ventilador1 = Ventilador('Ultra', 20.00, 5, '3 anos e 6 meses', 100, 180)
    print(f'1 - Ventilador\n {ventilador1}')

    ventilador2 = Ventilador('Mondial', 50.00, 5, '4 anos', 150, 180)
    print(f'O ventilador da {ventilador2.get_marca()} custa {ventilador2.get_preco()} reais\n')
    {ventilador2.set_preco(40.00)}
    print(f'O novo preco dos ventiladores da {ventilador2.get_marca()} sera {ventilador2.get_preco()} reais\n')

    microondas1 = Microondas('Midea', 120.00, 20, '8 anos', 0)
    print(f'1 - Microondas\n {microondas1}')

    microondas2 = Microondas('Quentinha', 200.00, 35, '10 anos', 0)
    {ventilador2.set_preco(210.00)}
    print(f'O novo preco dos microondas da {microondas2.get_marca()} sera {microondas2.get_preco()} reais\n')

    ventilador1.ligar(ventilador1.get_marca())
    microondas1.trocar_modos(microondas1.get_tempo_preparo())

