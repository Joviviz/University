import mysql.connector

""" 
def criar_db(): 
    try:
        db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Vieira.123'
    )

    mycursor = db.cursor()

    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS dv_xmen")

"""

def criar_bd():
        db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Vieira.123')

        mycursor = db.cursor()

        try:
               mycursor.execute("CREATE DATABASE IF NOT EXISTS db_xmen")
        
        except Exception as e:
               print("Something went wrong: {e}")
        
        finally:
               db.close()


def criar_tabelas():
        db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Vieira.123',
        database='db_xmen')

        mycursor = db.cursor()

        # Criar tabelas
        try:
               mycursor.execute("""
                        CREATE TABLE IF NOT EXISTS Estudante(
                            ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            nome VARCHAR(100) NOT NULL,
                            idade SMALLINT UNSIGNED NOT NULL,
                            habilidades VARCHAR(500) NOT NULL,
                            nivel_poder SMALLINT UNSIGNED NOT NULL,
                            equipe VARCHAR(50) NOT NULL,
                            status_matricula VARCHAR(20) NOT NULL
                            );""")
               
        except Exception as e:
               print("Something went wrong: {e}")

if __name__ == "__main__":

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Vieira.123',
    )


    mycursor = db.cursor()

    criar_bd()
    criar_tabelas()

    
    # mycursor.execute(f"INSERT INTO Estudante (nome, idade) VALUES (%s, %s)", ("Hulk", 50))
    