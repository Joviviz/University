"""                 Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Com base nos conceitos de POO (Programação Orientada a Objetos),
e inheritance (herança), implemente a entidade veículo com as
especializações de carro e moto.

- Precisamos trabalhar com as características:
valor, modelo, quilometragem, quantidade de portas e cilindradas.

 Implemente estes itens:
1- Crie a superclasse Veiculo e o construtor (__init__) com os atributos comuns:
   valor, modelo (Corolla, Argo etc.) e km que indica a quilometragem. Teste
2- Crie alguns métodos gets e sets.
3- Antes do método main, crie a subclasse Carro, que herda da superclasse Veiculo. E o
   construtor com os atributos valor, modelo, km e qtd_portas. E os métodos get e set.
4- Crie três instâncias da subclasse Carro com quatro, três e dois argumentos, teste
5- Na classe Carro, sobrescreva o método __str__ do Python, ele retorna todos os dados
   (atributos), teste
6- Antes do método main, crie a subclasse Moto, que herda a superclasse Veiculo. E o
   construtor com os três atributos comuns e o atributo cilindradas. E os métodos get e set
7- Crie duas instâncias (objetos) da classe Moto com quatro e três argumentos. Teste
8- Utilize o método vars() para acessar os atributos de Carro e Moto num dicionário.
   Ex.: print(vars(objeto))
9- Use o método __dict__ para acessar os atributos de Carro e Moto num dicionário.
   Ex.: print(objeto.__dict__)
10- Crie o método (def) atualiza valor, ele recebe um valor em reais e não retorna nada.
    O método acrescenta o valor recebido ao valor de qualquer veículo. Teste.
10b- Refaça o item anterior com críticas (filtros) dentro da função.
11- Crie o método atualiza_valor_pct, ele recebe a porcentagem (5, 10, 20 etc) e não
    retorna nada. O método atualiza o valor de qualquer veículo. Faça crítica e teste.
12- Crie o método situacao do veículo para mostrar se é veículo zero, veículo seminovo
    ou veículo usado. O veiculo zero tem km igual a zero, seminovo se tiver até 20000 Km e
    veículo usado se tiver mais que 20000 Km. Use o método com os objetos criados.
13- Crie o método situacao_2 para substituir a mensagem 'Veículo zero' por uma mensagem
    mais específica 'Carro zero' ou 'Moto zero' e assim sucessivamente com as outras
    mensagens. Teste

"""


# Nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Veiculo:            # Três formas equivalentes de criar classe
# class Veiculo():
class Veiculo(object):      # Superclasse
    def __init__(self, valor, modelo, km=1):  # Construtor com valor default
        self.valor = valor                    # Atributos de instância
        self.modelo = modelo
        self.km = km
    def get_valor(self):                      # Consulta
        return self.valor
    def set_valor(self, novo_valor):          # Sem crítica
        self.valor = novo_valor
    # def set_valor(self, valor):             # Com crítica
    #     if valor > 0:
    #         self.valor = valor
    #     else:
    #         print('Valor negativo.')
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_km(self):
        return self.km
    def set_km(self, nova_km):
        self.km = nova_km
    # def atualiza_valor(self, vlr_aumento):     # Sem crítica
    #     self.valor = self.valor + vlr_aumento  # self.valor += vlr_aumento
    def atualiza_valor(self, vlr_aumento):       # Com uma crítica
        if vlr_aumento > 0:
            self.valor += vlr_aumento
            # self.valor = self.valor + vlr_aumento
        else:
            print('Erro: valor negativo.')
    # def atualiza_valor(self, vlr_aumento):     # Com duaus críticas
    #     # if isinstance(vlr_aumento, float) or isinstance(vlr_aumento, int):
    #     if isinstance(vlr_aumento, (int, float)):  # 2 linhas equivalentes
    #         if vlr_aumento > 0:
    #             self.valor += vlr_aumento
    #             # self.valor = self.valor + vlr_aumento
    #         else:
    #             print('Erro: valor negativo.')
    #     else:
    #         print('Erro: tipo deve ser int ou float.')
    def atualiza_valor_pct(self, pct):
        if pct > 0:
            self.valor = self.valor + self.valor * pct / 100
            # self.valor += self.valor * pct / 100  # Equivalente a anterior
        else:
            print('Erro: porcentagem negativa.')
    def situacao(self):
        if self.km == 0:
            print('Veiculo zero.')
        elif self.km <= 20000:
            print("Veículo seminovo.")
        else:
            print('Veículo usado.')
    def situacao_2(self):
        nome_classe = self.__class__.__name__  # O nome da classe de um objeto
        print(f'- Modelo: {self.modelo}, R$ {self.valor}:')
        if nome_classe == "Carro":
            if self.km == 0:
                print('Carro zero.')           # Gera a mensagem específica
            elif self.km <= 20000:
                print('Carro seminovo.')
            else:
                print('Carro usado.')
        elif nome_classe == "Moto":
            if self.km == 0:
                print('Moto zero.')            # Gera a mensagem específica
            elif self.km <= 20000:
                print('Moto seminovo.')
            else:
                print('Moto usado.')
    def situacao_3(self):
        tpo_veiculo = self.__class__.__name__  # O nome da classe de um objeto
        print(f'- Modelo: {self.modelo}, R$ {self.valor}:')
        if self.km == 0:
            print(tpo_veiculo, 'zero.')        # Gera a mensagem específica
        elif self.km <= 20000:
            print(tpo_veiculo, 'seminovo.')
        else:
            print(tpo_veiculo, 'usado.')


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):   # Sintaxe
class Carro(Veiculo):                     # A subclasse Carro herda da superclasse Veiculo
    def __init__(self, valor, modelo, km=1, qtd_portas=4):  # Construtor com valor default
        super().__init__(valor, modelo, km)            # Chama o construtor da superclasse
        self.qtd_portas = qtd_portas
    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd):
        self.qtd_portas = nova_qtd

    def __str__(self):                                      # Método dunder ou mágico
        # s = "Valor: {:.2f}, modelo: {}, Km: {}, Qtd. portas: {}" \
        #     .format(self.valor, self.modelo, self.km, self.qtd_portas)      # .format
        s = f"Valor: {self.valor:.2f}, modelo: {self.modelo}, Km: {self.km}, " \
            f"qtd. portas: {self.qtd_portas}"                                 # f-string
        return s


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):  # Sintaxe
class Moto(Veiculo):                     # A subclasse Moto herda da superclasse Veiculo
    def __init__(self, valor, modelo, km=1, cilindradas=0):  # Construtor
        super().__init__(valor, modelo, km)         # Chama o construtor da superclasse
        self.cilindradas = cilindradas
    def get_cilindradas(self):
        return self.cilindradas
    def set_cilindradas(self, novo_valor):
        self.cilindradas = novo_valor


if __name__ == '__main__':
    c1 = Carro(99000.00, "Civic", 1000, 4)  # Instancia objeto da subclasse
    print('- Carro 1:\n', c1)               # print(c1.__str__())
    print(f'Valor: {c1.get_valor():.2f}')   # Duas casas decimais
    print('Modelo:', c1.get_modelo())
    print('Qtd. portas', c1.get_qtd_portas())
    c2 = Carro(100000.00, 'Corolla', 5000)  # Três argumentos
    print('- Carro 2:\n', c2)
    print(f'Valor: {c2.get_valor():.2f}')
    print('Modelo:', c2.get_modelo())
    print('Qtd. portas', c2.get_qtd_portas())
    c3 = Carro(70000.00, 'HB20')            # Dois argumentos
    print('- Carro 3:\n', c3)
    print(f'Valor: {c3.get_valor():.2f}')
    print('Modelo:', c3.get_modelo())
    print('Qtd. portas', c3.get_qtd_portas())
    c3.set_valor(88000.00)
    print(f'Preço alterado: {c3.get_valor():.2f}')
    m1 = Moto(22000.00, "CBS", 12000, 400)  # Quatro argumentos
    print('- Moto 1:\n', m1)
    # <Veiculo_aula2.veiculo_moto.Moto object at 0x000002CFD014E0D0>
    print('Modelo:', m1.get_modelo())
    print('Cilindradas:', m1.get_cilindradas())
    m2 = Moto(32000.00, "CBS", 0)           # Três argumentos
    print('- Moto 2:\n', m2)
    print('Modelo:', m2.get_modelo())
    print('Cilindradas:', m2.get_cilindradas())
    m2.set_valor(44000.00)
    print(f'Preço alterado: {c3.get_valor():.2f}')
    print("Dados do carro e moto num dicionário (vars ou __dict__)")
    print(vars(c1))                         # Métodos do Python
    print(c1.__dict__)                      # Métodos do Python
    # {'valor': 990000, 'modelo': 'Civic', 'km': 1000, 'qtd_portas': 4}
    print(vars(m1))
    print(m1.__dict__)
    # {'valor': 22000, 'modelo': 'CBS', 'km': 12000, 'cilindradas': 400}
    c1.atualiza_valor(1000.0)               # Argumento correto
    c1.atualiza_valor(1000)                 # Argumento correto
    c1.atualiza_valor(-1000)                # Argumento errado, msg erro
    print(c1.__dict__)                      # Teste
    m1.atualiza_valor(450.00)               # Argumento correto
    print(m1.__dict__)                      # Teste
    c3.atualiza_valor_pct(10)               # Argumento correto
    c3.atualiza_valor_pct(-10)              # Argumento errado, msg erro
    print(vars(c3))
    m2.atualiza_valor_pct(20)               # Argumento correto
    print(m2.__dict__)                      # Teste
    c1.situacao()
    m2.situacao()
    c1.situacao_2()         # Chama o método com objeto da subclasse Carro
    m2.situacao_2()         # Chama o método com objeto da subclasse Moto
