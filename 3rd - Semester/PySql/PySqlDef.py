import mysql.connector

def create_database():
    conexao_db = mysql.connector.connect(
        user='root',
        password= 'super',
        host='127.0.0.1'
    )
    print('Conexao:', conexao_db)
    cursor = conexao_db.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS db_loja_2')
    cursor.close()
    conexao_db.close()
    print('\nConexao Fechada.\n')

def create_connection():
    conn = mysql.connector.connect(
        user='root',
        password='Vieira.123',
        database= 'db_loja_2'
    )
        
    print('Conexao: ',conn)
    return conn

def create_table():
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS tb_produto(
            idt INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(45) NOT NULL UNIQUE,
            preco DECIMAL(9,2) NOT NULL,
            dta_validade DATE NULL
        )'''
        )

def insert():
    a_nome = input('Nome: ')
    a_preco = float(input('Preco'))
    a_data = input('Data: aaaa-mm-dd')
    
    cursor.execute(
        f''' INSERT INTO tb_produto (nome, preco, dta_validade)
            VALUES('{a_nome}',{a_preco},'{a_data}')
    ''')

    print('Registros inseridos:', cursor.rowcount)
    conexao.commit()

def select():
    cursor.execute(
        'SELECT * FROM tb_produto'
    )
    l_registros = cursor.fetchall()
    print('- Lista de Tuplas:', l_registros)
    print('Quantidade de resgistros no select (rowcount):', cursor.rowcount)

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexao Fechada.\n')


if __name__ == '__main__':
    #create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    #create_table()
    insert()
    