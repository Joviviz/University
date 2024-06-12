import mysql.connector

# Pronto - Cria BD e suas Tabelas
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

                mycursor.execute("""
                        CREATE TABLE IF NOT EXISTS Estudante(
                            ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
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
          

if __name__ == "__main__":
    criar_bd()

    print("Bem vindo ao Sistema de Dados dos XMEN!")
    print("Escolha uma opção: ")
    opcao = int(input("1 - Cadastrar Estudante\n"))

    match opcao:
            case 1:
                  cadastrar_estudante()
            case _:
                  print("Opção não disponível")


    