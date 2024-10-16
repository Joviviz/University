import mysql.connector
from mysql.connector import Error

# Cria BD e suas Tabelas
def criar_bd():
    try:
        db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Vieira.123')

        mycursor = db.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS db_xmen")
        print("Base de Dados criada com sucesso!")

        db.database = "db_xmen"

        # Tabela Estudante - Pronto
        mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Estudante (
                    ID_estudante INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(100) NOT NULL,
                    idade SMALLINT UNSIGNED NOT NULL,
                    habilidade VARCHAR(500) NOT NULL,
                    nivel_poder SMALLINT UNSIGNED NOT NULL,
                    equipe VARCHAR(50) NOT NULL,
                    status_matricula VARCHAR(20) NOT NULL
                    );""")
        
                    
        print("Tabelas criadas com Sucesso!")
    
    except Exception as e:
        print("Something went wrong: {e}")
    
    finally:
        if db.is_connected():
            mycursor.close()
            db.close()
    
# Pronto - Corrige a entrada de dados no Cadastro
def corrigir_entrada(mensagem, tipo, validador=None):
    while True:
            
        # Recebemos o inputo do Usuário removendo os espaços vazios com ".strip()"
        entrada = input(mensagem).strip()

        if not entrada:
                # Confere se a entrada está vazia
                print("Por favor, insira um valor correto. A entrada está vazia!")
                continue
        
        try:
                # Confere se o tipo e a entrada sao compativeis e retorna para a outra função
                valor = tipo(entrada)
                
                # Chama a função validar_negativo
                if validador: # Se a função validadora foi fornecida
                    validador(valor) # Chama a função

                return valor

        except ValueError:
                print("Por favor, insira um valor correto!")

# Pronto - Confere se o valor é negativo
def validar_negativo(numero):
    if numero < 0:
            print("Esse valor não pode ser negativo")
            raise ValueError("Esse valor não pode ser negativo")
    return numero

# Pronto - Entrada -> Cadastro
def cadastrar_estudante():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Vieira.123',
            database='db_xmen')
    
        mycursor = db.cursor()
        
        nome = corrigir_entrada("Nome: ", str)
        idade = corrigir_entrada("Idade: ", int, validar_negativo)
        habilidade = corrigir_entrada("Descreva a habilidade: ", str)
        nivel_poder = corrigir_entrada("Nível de Poder: ", int, validar_negativo)
        equipe = corrigir_entrada("Equipe: ", str)
        status_matricula = corrigir_entrada("Status de Matrícula: ", str)

        mycursor.execute("""INSERT INTO Estudante
                            (nome, idade, habilidade, nivel_poder, equipe, status_matricula)
                            VALUES (%s, %s, %s, %s, %s, %s)""", 
                            (nome, idade, habilidade, nivel_poder, equipe, status_matricula))
        db.commit()
        print("Estudante cadastrado com sucesso")
    
    except Exception as e:
        print("Something went wrong: {e}")

    finally:
        if db.is_connected():
            mycursor.close()
            db.close()
          
# Pronto - Consulta de Dados
def consulta_de_dados():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Vieira.123',
            database='db_xmen')

        mycursor = db.cursor()

        print("Consulta de Dados\n")
        print("Deixe um espaço em branco para não pesquisar o atributo\n")

        nome = input("Procurar - Nome: ").strip()
        idade = input("Procurar - Idade: ").strip()
        habilidade = input("Procurar - Descreva a habilidade: ").strip()
        nivel_poder = input("Procurar - Nível de Poder: ").strip()
        equipe = input("Procurar - Equipe: ").strip()
        status_matricula = input("Procurar - Status de Matrícula: ").strip()
        2
        print("")

        pesquisa = "SELECT * FROM Estudante WHERE 1=1"
        valores = []

        if nome:
            pesquisa += " AND nome LIKE %s"
            valores.append(f'%{nome}')
        
        if idade:
            pesquisa += " AND idade LIKE %s"
            valores.append(f'%{idade}')
        
        if habilidade:
            pesquisa += " AND habilidade LIKE %s"
            valores.append(f'%{habilidade}')
        
        if nivel_poder:
            pesquisa += " AND nivel_poder LIKE %s"
            valores.append(f'%{nivel_poder}')
        
        if equipe:
            pesquisa += " AND equipe LIKE %s"
            valores.append(f'%{equipe}')
        
        if status_matricula:
            pesquisa += " AND status_matricula LIKE %s"
            valores.append(f'%{status_matricula}')

        
        mycursor.execute(pesquisa, valores)
        variaveis = mycursor.fetchall()

        for row in variaveis:
            print("ID :", row[0])
            print("Nome :", row[1])
            print("Idade :", row[2])
            print("Habilidade :", row[3])
            print("Nível de poder :", row[4])
            print("Equipe :", row[5])
            print("Status Matrícula :", row[6], "\n")

    except Exception as e:
            print("Something went wrong: {e}")
    finally:
        if db.is_connected():
            mycursor.close()
            db.close()
    



if __name__ == "__main__":
    criar_bd()

    print("Bem vindo ao Sistema de Dados dos XMEN!")
    print("Escolha uma opção: ")
    print("1 - Cadastrar Estudante\n2 - Consultar Tabelas")
    print("3 - Lorum\n4 - Lorum")
    opcao = int(input(""))

    match opcao:
            case 1:
                  cadastrar_estudante()
            case 2:
                  consulta_de_dados()
            case _:
                  print("Opção não disponível")


    