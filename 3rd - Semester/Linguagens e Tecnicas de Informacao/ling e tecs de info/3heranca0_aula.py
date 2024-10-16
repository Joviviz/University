"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Com base nos conceitos de POO, vamos trabalhar com duas classes (entidades).
Implemente a entidade funcionário com estas características: cpf, nome e salario.
E a entidade gerente com estas características: cpf, nome, salario, senha e
quantidade de funcionários que ele gerencia.

- Implemente estes itens:
1- Crie a classe Funcionario e o construtor, def __init___ (self, ...), da classe
   com os atributos cpf, nome e salario
2- Crie uma instância (objeto) da classe com os dados necessários (f1 = Funcionario()), teste
3- Crie alguns métodos get e set. Teste
4- Crie um segundo funcionário passando apenas o cpf e o nome. Teste
5- Sobrescreva o método __str__. Ele recebe o objeto e retorna os dados do funcionário. Teste.
6a- Crie a classe Gerente e o construtor com os atributos cpf, nome, salario, senha e a
   quantidade de funcionários que ele gerencia.
6b-Crie uma instância (objeto) da classe Gerente com os dados necessários, teste
7- Crie alguns métodos gets e sets. Teste
8- Mostre todos os dados (atributos) do objeto g1 da classe Gerente, conseguiu usando o __str__?
9- Crie o método autentica na classe Gerente. Ele recebe o objeto, o usuário digita a senha
   e verifica se a senha digitada é igual a senha armazenada na memória (self.senha).
   imprime: "Acesso permitido." ou "Acesso negado." e retorna o valor booleano True ou False.
10- Use o método autentica para o gerente instanciado (objeto g1).
11- Use o método autentica para o funcionario instanciado (objeto f1). Por quê deu erro?
12- Crie outra instância (objeto g2) da classe Gerente com os dados necessários.
13- Use o método __str__ para o gerente (objeto g2). Por quê mostrou endereço hexadecimal?
14- Use todos os métodos da classe Gerente para o gerente g2.

"""

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Funcionario:
# class Funcionario():
class Funcionario(object):  # Superclasse  # Três formas equivalentes de criar a classe
    def __init__(self, cpf, nome, salario=0.0):  # Construtor com valor default
        self.cpf = cpf                           # Atributos de instância
        self.nome = nome
        self.salario = salario
    def get_cpf(self):                           # Consulta
        return self.cpf
    def set_cpf(self, novo_cpf):                 # Altera na memória
        self.cpf = novo_cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def __str__(self):                          # Método mágico ou método dunder
        # s = 'Nome: ' + self.nome+ ',  CPF: ' + self.cpf+', salário: '+str(self.salario)
        # s = "Nome: {}, CPF: {}, salario: {:.2f}"
        #           .format(self.nome, self.cpf, self.salario)
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}"  # f-string
        return s                                # As linhas anteriores são equivalentes
        # return f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}"


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Gerene:
# class Gerente():
class Gerente(object):  # Superclasse  # Três formas equivalentes de criar a classe
    def __init__(self, cpf, nome, salario, senha, qtd_gerencia=1):  # valor default
        self.cpf = cpf                          # Atributos de instância
        self.nome = nome
        self.salario = salario
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia
    def get_cpf(self):                          # Consulta
        return self.cpf
    def set_cpf(self, novo_cpf):                # Altera
        self.cpf = novo_cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd
    def autentica(self):            # Solução 1
        senha = input("Senha: ")    # A variável senha só vale dentro do método autentica
        if senha == self.senha:     # O self.senha vale em toda a classe Gerente
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False


if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.00)   # Cria o objeto f1, chama o construtor
    print(f1)                                   # print(f1.__str__())   # Teste
    # <__main__.Funcionario object at 0x00000159D5FFB2C8>
    print(f'- Funcionário 1:\nNome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print('Salário:', f1.get_salario())
    f1.set_nome('Vinícius')
    print(f'Nome alterado: {f1.get_nome()}')
    f2 = Funcionario('12345', 'Ana')            # Cria o objeto f2, chama o construtor
    print(f2)                                   # print(f1.__str__())   # Teste
    print(f'- Funcionário 2:\nNome: {f2.get_nome()}')
    print(f'CPF: {f2.get_cpf()}')
    print('Salário:', f2.get_salario())
    f2.set_nome('Emily')
    print(f'Nome alterado: {f2.get_nome()}')
    print(f1.__str__())               # print(f1)                        # Teste
    print(f2.__str__())               # print(f2)                        # Teste
    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)  # g1 é um objeto da classe Gerente
    print(g1)                                      # print(g1.__str__())   # Teste
    # <heranca0_gerente.Gerente object at 0x000001C23ECFB0A0>
    print(f'- Gerente 1:\nCPF: {g1.get_cpf()}')
    print('Nome:', g1.get_nome())
    print('Salário:', g1.get_salario())
    print('Qtd. funcionários:', g1.get_qtd_gerencia())
    g1.set_nome('Alice')
    print(f'Nome alterado: {g1.get_nome()}')
    print(g1.__str__())                         # print(g1), conseguiu usando o __str__?
    r = g1.autentica()                          # O método retorna True ou False
    print(r)
    print(g1.autentica())                       # Linhas equivalentes
    # r = f1.autentica()                    # Erro, Funcionario não tem método autentica
    # AttributeError: 'Funcionario' object has no attribute 'autentica'
    g2 = Gerente('34', 'Paulo', 5000.0, 's2', 3)
    print(g2.__str__())                         # print(g2), conseguiu usando o __str__?
    print('- Gerente 2:\nCPF:', g2.get_cpf())
    print('Nome:', g2.get_nome())
    print('Salário:', g2.get_salario())
    print('Qtd. funcionários:', g2.get_qtd_gerencia())
