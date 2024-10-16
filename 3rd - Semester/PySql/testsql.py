import mysql.connector

def create_database():
    conexao_db = mysql.connector.connect(
        user='root',
        host='localhost',
        password='uniceub'
    )
    print('Conexao: ', conexao_db)
    
    cursor_db = conexao_db.cursor()
    cursor_db.execute('CREATE DATABASE IF NOT EXISTS db_loja_2')

    cursor_db.close()
    conexao_db.close()
    print('Conexao fechada')

def create_connection():
    conexao = mysql.connector.connect(
        user='root',
        host='localhost',
        password='uniceub'
    )
    print('Conexao: ', conexao)
    return conexao

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_produto(
            idt INT NOT NULL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL UNIQUE,
            preco DECIMAL(9,2) NOT NULL,
            dta_validade DATE NULL
            )
        ''')

def insert_table():
    a_nome = input('Nome: ')
    a_preco = float(input('Preco: '))
    a_data = input('Data: aaaa - mm - dd')

    cursor.execute('''
    INSERT INTO tb_produto (nome, preco, dta_validade)
    VALUES('{a_nome}','{a_preco}','{a_data}')
    ''')
    print('Resgistros inseridos:', cursor.rowcount)
    conexao.commit()

def select():
    cursor.execute('SELECT * FROM tb_produtos')

    l_registros = cursor.fetchall

    print('Lista de Tuplas: ', l_registros)

def close_connection():
    cursor.close()
    conexao.close()
    print('Conexao Fechada')

if __name__ == '__main__':
    conexao=create_connection()
    cursor=conexao.cursor()
