"""            Comentários de várias linhas.
  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Com base nos conceitos de POO (Programação Orientada a Objetos), implemente
a entidade aluno com estas características: nome, mensalidade, idade.

- Implemente:
1- Crie um novo projeto, um programa .py e a classe Aluno.
2- Crie o construtor da classe com os atributos: nome, mensalidade, idade
3- No main, crie (instancie) pelo menos dois objetos da classe Aluno, teste
4- Crie os métodos gets (consulta) e sets (altera)
5- Use (teste) os métodos gets para os objetos criados
6- Use (teste) os métodos sets para os objetos criados
7- Crie o método mostra_dados. Não recebe e não retorna nada. Mostra os atributos. Teste
8- Crie o método retorna_dados, retorna todos os dados (atributos) concatenados. Teste
9- Crie o método aumento_mensalidade_valor, ele recebe o objeto e o valor do aumento. Teste
10- Crie o método aumento_mensalidade_porcentagem (recebe: 10%, 15% etc.). Teste
11- Crie o método que verifica se o aluno pode tirar a CNH e mostre mensagem apropriada.
12- Altere o construtor com estes valor default (padrão): mensalidade = 1000.0, idade = 18.
13- No main, crie (instancie) mais um objeto da classe Aluno, passando apenas o nome, teste

"""

class Aluno:            # class Aluno():           # class Aluno(object):
    # def __init__(self, nome, mensalidade, idade):  # Método construtor
    def __init__(self, nome, mensalidade=1000.0, idade=18):  # Valores default
        self.nome = nome                # Atributos
        self.mensalidade = mensalidade  # self.nome_atributo = parametro
        self.idade = idade
    def get_nome(self):                 # Métodos gets (consulta)
        return self.nome
    def set_nome(self, novo_nome):      # Métodos sets (altera)
        self.nome = novo_nome
    def get_mensalidade(self):          # Consulta o valor do atributo e retorna
        return self.mensalidade
    def set_mensalidade(self, valor):   # Altera o valor do atributo e não retorna
        self.mensalidade = valor
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def mostra_dados(self):                     # Solução 1, com atributos
        print('- Nome:', self.nome)
        print('Mensalidade:', self.mensalidade)
        print('Idade:', self.idade)
    def mostra_dados2(self):                   # Solução 2, com métodos
        print('- Nome:', self.get_nome())
        print('Mensalidade:', self.get_mensalidade())
        print('Idade:', self.get_idade())
    def retorna_dados(self):                    # Métodos funcionais
        # dados = self.nome + ', ' +str(self.mensalidade) + ', ' +str(self.idade)
        # dados = '%s, %f, %d' % (self.nome, self.mensalidade, self. idade)
        # dados = '{}, {}, {}'.format(self.nome, self.mensalidade, self.idade)
        # dados = f'{self.nome}, {self.mensalidade}, {self.idade}'
        dados = f'{self.get_nome()}, {self.get_mensalidade()}, {self.get_idade()}'
        return dados
        # return f'{self.nome}, {self.mensalidade}, {self.idade}'  # Equivalente
    def aumento_mensalidade_valor_1(self, aumento):     # Solução 1
        self.mensalidade += aumento
        # self.mensalidade = self.mensalidade + aumento
    def aumento_mensalidade_porcentagem(self, pct):
        self.mensalidade += self.mensalidade * pct / 100
        # self.mensalidade = self.mensalidade + self.mensalidade * pct / 100
    def pode_cnh(self):
        if self.idade >= 18:
            print("Pode CNH.")
        else:
            print("Não pode CNH.")


if __name__ == '__main__':                # Atalho: mai <tab>
    aluno1 = Aluno('Paulo', 1100.00, 21)  # Chama o método __init__ (construtor)
    print(aluno1)  # Mostra o endereço hexadecimal onde o objeto aluno1 foi armazenado
    # <aluno_4.Aluno object at 0x0000015D8FF16FD0>
    aluno2 = Aluno('Carla', 900.00, 20)
    print(aluno2)   # Mostra que é um objeto da classe Aluno e o endereço hexadecimal
    # <aluno_4.Aluno object at 0x0000015D8FF16F70>
    print("- Aluno 1:")
    print("Nome:", aluno1.get_nome())  # print(nome_objeto.nome_metodo()) Retorna um dado
    print("Mensalidade:", aluno1.get_mensalidade())
    print("Idade:", aluno1.get_idade())
    print("- Aluno 2:")
    print(f"Nome: {aluno2.get_nome()}")         # print(nome_objeto.nome_metodo())
    print(f"Mensalidade: {aluno2.get_mensalidade()}")
    print(f'Idade: {aluno2.get_idade()}')
    # nome1 = "Ailton Pinheiro"
    nome1 = input("Novo nome: ")                        # Solução 1
    aluno1.set_nome(nome1)                # nome_objeto.nome_metodo() - não retorna dado
    # aluno1.set_nome(input("Novo nome: "))  # Equivalente as duas linhas anteriores
    print('Nome atualizado:', aluno1.get_nome())        # Verifica (testa)
    aluno2.set_nome("Alice")                            # Solução 2
    print('Nome atualizado:', aluno2.get_nome())        # Verifica (testa)
    aluno1.set_mensalidade(1200.00)
    print("Mensalidade atualizada:", aluno1.get_mensalidade())  # Verifica (testa)
    aluno1.mostra_dados()                 # nome_objeto.nome_metodo() - não retorna dado
    aluno2.mostra_dados()
    aluno1.mostra_dados2()
    aluno2.mostra_dados2()
    print('Dados concatenados do aluno 1:\n', aluno1.retorna_dados())
    print('Dados concatenados do aluno 2:\n', aluno2.retorna_dados())
    aluno1.aumento_mensalidade_valor_1(110)
    print('Nova mensalidade:', aluno1.get_mensalidade())    # Verificação (teste)
    aluno2.aumento_mensalidade_valor_1(105)
    print('Nova mensalidade:', aluno2.get_mensalidade())    # Verificação (teste)
    aluno2.aumento_mensalidade_porcentagem(10)              # Aumento de 10%
    print('Nova mensalidade:', aluno2.get_mensalidade())    # Teste
    aluno1.pode_cnh()
    aluno2.pode_cnh()
    aluno3 = Aluno('Ailton')              # Chama o construtor passando somente o nome
    aluno3.mostra_dados()                 # Teste
    aluno4 = Aluno('Ana', 800)
    aluno4.mostra_dados()                 # Teste
