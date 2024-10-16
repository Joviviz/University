"""                 Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Com base nos conceitos de Programação Orientada a Objetos (POO)
e inheritance (herança), implemente a entidade conta corrente com as
especificidades de conta corrente de uma pessoa física e de uma pessoa
jurídica.
Levante as características comuns e as características
específica de uma conta corrente de pessoa física e de conta corrente
de pessoa jurídica.

- Algumas características de uma conta corrente:
nome, saldo, gênero, CPF, modalidade de PJ e CNPJ

- Implemente estes itens:

1- Crie a superclasse Conta
2- Crie o método construtor com os atributos nome e saldo, teste
3- Crie os métodos gets e sets da superclasse, teste
4- Sobrescreva o método __str__ para ele retornar os atributos, teste
5- Crie a subclasse Conta pessoa física
6- Crie o método construtor com os atributos nome, saldo, genero e cpf
7- Crie uma instância (objeto) de Conta_PF, teste
8- Crie os métodos get e set
9- Use os métodos da subclasse Conta_PF
10- Use o método do Python vars.              Sintaxe: print(vars(objeto))
11- Use o método do Python __dict__                    print(objeto.__dict__)
12- Crie a subclasse Conta pessoa jurídica
13- Crie o método construtor com os atributos nome, saldo, modalidade e cnpj
14- Crie uma instância (objeto) de Conta_PJ
15- Crie os método get e set, teste
16- Crie o método deposito, ele recebe o valor do depósito e atualiza o saldo, teste
17- Crie o método retirada, ele recebe o valor da retirada e atualiza o saldo, teste
18- Refaça o método retirada usando RNs (Regras de Negócios) bancárias. Teste

"""


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Conta:
# class Conta():
class Conta(object):                        # Superclasse
    def __init__(self, nome, saldo=0.0):    # Construtor da superclasse com default
        self.nome = nome                    # Atributos de instância (objeto)
        self.saldo = saldo
    def get_nome(self):                     # Consulta
        return self.nome
    def set_nome(self, novo_nome):          # Altera
        self.nome = novo_nome
    def get_saldo(self):
        return self.saldo
    def __str__(self):                      # Sobrescreve o método __str__ do Python
        # s = 'Nome: ' + self.nome + ', R$ ' + str(self.saldo)  # Concatenação
        s = f'Nome: {self.nome}, R$ {self.saldo}'               # f-string
        return s
    def deposito(self, valor):              # Métodos funcionais
        self.saldo += valor                 # self.saldo = self.saldo + valor
    def retirada(self, valor):              # Sem RN (Regra de Negócio)
        self.saldo -= valor                 # self.saldo = self.saldo - valor
    def retirada_rn(self, valor):           # RN obrigatória (natural do banco)
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):     # Sintaxe
class Conta_PF(Conta):             # Subclasse Conta_PF herda da superclasse Conta
    def __init__(self, nome, saldo=0.0, genero='m', cpf=''):  # Valores default
        super().__init__(nome, saldo)       # Chama o construtor da superclasse
        self.genero = genero
        self.cpf = cpf
    def get_genero(self):                   # Consulta
        return self.genero
    def set_genero(self, novo_genero):      # Altera
        self.genero = novo_genero
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf



""" - As principais modalidades de PJ:
1 - MEI (Microempreendedor Individual)
2 - ME – Microempresa
3 - EPP (Empresa de Pequeno Porte)
4 - EI (Empresário Individual) 
5 - EIRELI (Empresa Individual de Responsabilidade Limitada)
6 - Sociedade Limitada – LTDA
7 - Sociedade Anônima (SA)                                  """

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):   # Sintaxe

class Conta_PJ(Conta):              # Subclasse Conta_PJ que herda da superclasse Conta
    def __init__(self, nome, saldo=0.0, modalidade='MEI', cnpj=''):  # Construtor
        super().__init__(nome, saldo)               # Chama o construtor da superclasse
        self.modalidade = modalidade
        self.cnpj = cnpj
    def get_modalidade(self):
        return self.modalidade
    def get_cnpj(self):
        return self.cnpj
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj


if __name__ == '__main__':
    c = Conta('Alice')                  # Chama o construtor da classe Conta
    print(c)                            # print(c.__str__())
    print('- Superclasse:\nNome:', c.get_nome())  # Métodos da superclasse
    print('Saldo:', c.get_saldo())
    c.set_nome('Emily')
    print('Nome alterado:', c.get_nome())
    print(c.__str__())                  # print(c)
    pf1 = Conta_PF('Ana', 3000.0, 'f', '1234')  # Cria um objeto (instância) da subclasse
    print(pf1)                          # Chama o método __str__()
    print('- Pessoa Física 1:\nNome:', pf1.get_nome())  # Método na superclasse
    print("Saldo:", pf1.get_saldo())
    pf2 = Conta_PF('Ailton', 7000.0)    # Cria um objeto (instância) da subclasse Conta_PF
    print(pf2)                          # Chama o método __str__()
    print('- Pessoa Física 2:\nNome:', pf2.get_nome())  # Método na superclasse
    print("Saldo:", pf2.get_saldo())
    print('CPF:', pf2.get_cpf())        # Método da subclasse
    pf2.set_cpf('123456789')            # Altera
    print('CPF alterado:', pf2.get_cpf())  # Verifica alteração
    print('Saída usando as funções vars e __dict__ do Python:')
    print(vars(pf2))                    # Usa os métodos do Python
    print(pf2.__dict__)
    # {'nome': 'Ana', 'saldo': 3000.0, 'genero': 'm', 'cpf': ''}
    pj1 = Conta_PJ('Café ABC', 15000.0)  # Cria um objeto (instância) da subclasse Conta_PJ
    print(pj1)
    print('- Pessoa Jurídica:\nNome:', pj1.get_nome())      # Método da superclasse
    print("Saldo:", pj1.get_saldo())
    print('CNPJ:', pj1.get_cnpj())                          # Método da subclasse
    print(pj1)
    print(vars(pj1))                                        # Usa os métodos do Python
    print(pj1.__dict__)
    pf1.deposito(11)                                        # Depósito
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())    # Verifica alteração
    pj1.deposito(22)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo())  # Verifica alteração
    pf1.retirada(10)                                        # Retirada sem RN
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())    # Verifica alteração
    pj1.retirada(21)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo())  # Verifica alteração
    pf1.retirada_rn(10)                                     # Retirada com RN
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())    # Verifica alteração
    pj1.retirada_rn(21)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo())  # Verifica alteração
    pj1.retirada_rn(20000.0)                                # Retirada, msg erro
    print('Saldo: ', pj1.get_saldo())                       # Verifica alteração
