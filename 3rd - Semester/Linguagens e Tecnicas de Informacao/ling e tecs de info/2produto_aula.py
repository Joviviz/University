"""            Comentários de várias linhas.
  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Com base nos conceitos de POO (Programação Orientada a Objetos),
implemente a entidade produto com estas características:
nome, valor de compra, valor de venda, quantidade em estoque
e quantidade mínima (realizar uma nova compra do produto).

Implemente estes itens:
1- Crie o arquivo .py e a classe Produto.
2- O construtor da classe com os atributos: nome, vlr_compra, vlr_venda,
   qtd_estoque, qtd_minima
3- No main, crie o primeiro objeto da classe com os dados. Teste
4- Crie os métodos gets e sets dos atributos: nome, qtd_estoque e qtd_minima. Teste.
5- Altere a quantidade minima para um valor digitado. Teste.
6- Faça pelo menos uma crítica nos métodos set_qtd_estoque e set_nome. Teste.
7- Crie (acrescente) o método set_vlr_compra com crítica. Teste
8- Sobrescreva o método __str__ . Ele não recebe nada e retorna todos os atributos. Teste.
9- Crie o método funcional lucro. Não recebe nada e retorna o valor do lucro do produto. Teste
10- Crie o método funcional atualiza_estoque. Ele recebe a quantidade vendida
    de produtos e atualiza o estoque. Ele não retorna nada, teste
11- Método funcional repor_produto. Recebe a quantidade adquirida de produtos e atualiza, teste
12- Crie o método alerta_estoque. Não recebe nada e retorna um valor booleano. Retorna True,
   se a quantidade em estoque for menor que a quantidade mínima. Senão, retorna False. Teste
13- Crie o segundo objeto da classe passando apenas o argumento nome do produto, teste
14- No main, crie mais um objeto da classe passando apenas o argumento nome
    e valor de compra. Teste
15- No main, crie mais um objeto da classe passando apenas o argumento nome e
    a quantidade em estoque. Teste
16- Crie o método maior_qtd, ele compara dois produtos quaisquer e mostra
    o produto que tem a maior qtd em estoque. Teste

"""


# Nome de classe: primeira letra de cada palavra com letra maiúscula
class Produto(object):
    # def __init__(self, nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima):
    #     self.nome = nome                      # Atributos de instância
    #     self.vlr_compra = vlr_compra
    #     self.vlr_venda = vlr_venda
    #     self.qtd_estoque = qtd_estoque
    #     self.qtd_minima = qtd_minima
    def __init__(self, nome, vlr_compra=0.0, vlr_venda=0.0, qtd_estoque=0,
        qtd_minima=0):              # Construtor com valor default (padrão)
        self.nome = nome            # Atributos de instância
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
    def get_nome(self):             # Modelo do método get (retorna o valor)
        return self.nome
    # def set_nome(self, novo_nome):  # Modelo do método set (altera o valor)
    #     self.nome = novo_nome
    def set_nome(self, novo_nome):            # Com crítica
        if type(novo_nome) == str:            # Duas linhas equivalentes
        # if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print('Erro: Nome deve ser string.')
    def get_vlr_compra(self):
        return self.vlr_compra
    # def set_vlr_compra(self, novo_valor):     # Sem crítica
    #     self.vlr_compra = novo_valor
    def set_vlr_compra(self, valor):
        # if type(valor) != int and type(valor) != float:  # linhas equivalentes
        if not type(valor) in (int, float):
            print('Erro: qtd. estoque deve ser int ou float.')
        else:
            self.vlr_compra = valor
    def get_qtd_estoque(self):
        return self.qtd_estoque
    # def set_qtd_estoque(self, novo_vlr):      # Sem crícia
    #     self.qtd_estoque = novo_vlr
    def set_qtd_estoque(self, novo_vlr):        # Com crítica
        if type(novo_vlr) == int:
        # if isinstance(novo_vlr, int):
            self.qtd_estoque = novo_vlr
        else:
            print('Erro: qtd. estoque deve ser int.')
    def get_qtd_minima(self):            # Modelo: get_nome_atributo(self):
        return self.qtd_minima
    def set_qtd_minima(self, novo_vlr):  # Modelo: set_nome_atributo(self, valor):
        self.qtd_minima = novo_vlr
    def __str__(self):                   # Sobrescreve o método especial __str__
        s = f"Nome: {self.nome}, {self.vlr_compra}, {self.vlr_venda}, " \
            f"{self.qtd_estoque}, {self.qtd_minima}"
        return s
    def lucro(self):
        vlr_lucro = self.vlr_venda - self.vlr_compra
        return vlr_lucro
    def atualiza_estoque(self, qtd_vendida):
        self.qtd_estoque -= qtd_vendida
        # self.qtd_estoque = self.qtd_estoque - qtd_vendida
    def repor_produto(self, qtd_comprada):
        self.qtd_estoque += qtd_comprada
        #  self.qtd_estoque = self.qtd_estoque + qtd_comprada
    def alerta_estoque(self):
        if self.qtd_estoque < self.qtd_minima:
            var = True
        else:
            var = False
        return var
    def maior_qtd(self, objeto2):  # O método recebe dois objetos   # Solução 1
        if self.qtd_estoque > objeto2.qtd_estoque:
            print("Maior qtd:", self.get_nome())
        elif objeto2.qtd_estoque > self.qtd_estoque:
            print("Maior qtd:", objeto2.get_nome())
        else:
            print('Valores iguais.')


if __name__ == '__main__':                  # Atalho: mai <tab>
    prod_1 = Produto("Arroz", 19.00, 27.50, 67, 20)  # Chama o __init__
    print(prod_1)                           # Chama o método __str__
    # print(prod_1.__str__())               # Duas linhas equivalentes.
    print('Produto 1:\nNome:', prod_1.get_nome())  # nome_objeto.nome_metodo()
    print('Qtd. estoque:', prod_1.get_qtd_estoque())
    print('Valor de compra:', prod_1.get_vlr_compra())  # nome_objeto.nome_metodo()
    print('Qtd. estoque:', prod_1.get_qtd_estoque())
    qtd = int(input("Quantidade minima: "))  # qtd = 22
    prod_1.set_qtd_minima(qtd)              # Ex.: nome_objeto.nome_metodo(valor)
    print('Qtd. minima alterado:', prod_1.get_qtd_minima())  # Teste
    prod_1.set_qtd_minima(23)               # Ex.: nome_objeto.nome_metodo(valor)
    print('Qtd. minima:', prod_1.get_qtd_minima())  # Teste
    prod_1.set_nome('Novo arroz')           # Argumento correto
    print('Nome alterado:', prod_1.get_nome())       # Teste
    prod_1.set_nome(15)                     # Argumento errado, int
    print('Nome, não alterou:', prod_1.get_nome())       # Teste
    prod_1.set_qtd_estoque(30)              # Argumento correto
    print('Qtd. estoque alterado:', prod_1.get_qtd_estoque())  # Teste
    prod_1.set_qtd_estoque('Nome')          # Argumento errado, str
    print('Qtd. estoque, não alterou:', prod_1.get_qtd_estoque())  # Teste
    prod_1.set_vlr_compra(22.00)            # Argumento corrreto
    print(f'Valor de compra: {prod_1.get_vlr_compra()}')  # Teste
    prod_1.set_vlr_compra('String')         # Argumento errado
    print(f'Valor de compra: {prod_1.get_vlr_compra()}')  # Teste
    print('Mostra dados:', prod_1)          # Duas linhas equivalentes
    print('Mostra dados:', prod_1.__str__())
    print("Lucro:", prod_1.lucro())
    prod_1.atualiza_estoque(3)              # O argumento é a quantidade vendida.
    print('Qtd. estoque:', prod_1.get_qtd_estoque())
    print('Mostra dados:', prod_1)          # Teste
    # situacao = prod_1.alerta_estoque()    # Solução 1, com variável
    # if situacao == True:
    if prod_1.alerta_estoque():             # Solução 2, sem variável
        print("Precisa comprar.")
    else:
        print("Não precisa comprar.")
    # O operador ternário equivalente ao if ... else ... anterior.  - Solução 3
    # Sintaxe: (se condicão verdadeira) if condição else (se condição falsa)
    print("Precisa comprar.") if prod_1.alerta_estoque() else print("Não precisa comprar.")
    prod_1.repor_produto(11)
    print('Qtd. estoque:', prod_1.get_qtd_estoque())  # Teste
    prod_2 = Produto("Feijão")              # Chama __init__, instancia o objeto prod_2
    print(prod_2)                           # Teste
    prod_3 = Produto('Café', 10.00)         # nome, preço de compra
    print(prod_3)
    # # prod_4 = Produto('Farinha', 0, 0, 20, 0)  # Solução 1, não é boa solução.
    prod_4 = Produto('Farinha', qtd_estoque=20)   # Solução 2, nome, quantidade em estoque
    print(prod_4)
    prod_1.maior_qtd(prod_2)                # prod_1 (self)  e  prod_2 (objeto2)
    prod_2.maior_qtd(prod_1)
    prod_2.maior_qtd(prod_3)
