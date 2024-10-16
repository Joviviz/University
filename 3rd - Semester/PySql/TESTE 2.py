import mysql.connector

def create_database():
    db_conexao = mysql.connector.connect(
        user='root',
        host='localhost',
        password='uniceub'
    )
    print('Conexao Estabelecida : ', db_conexao)

    db_cursor = db_conexao.cursor()
    db_cursor.execute('CREATE DATABASE IF NOT EXISTS db_loja_2')

    db_cursor.close()
    db_conexao.close()
    print('Conexao Fechada')

def create_connection():
    conn = mysql.connector.connect(
        user='root',
        host='localhost',
        password='uniceub',
        database= 'db_loja_2'
    )
    print('Conexao Estabelecida: ', conn)
    return conn

def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_produto(
        idt INT NOT NULL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL UNIQUE,
        preco DECIMAL(9,2) NOT NULL,
        dta_validade DATE NULL
    )
    ''')

def insert():
    a_nome = input('Nome: ')
    a_preco = float(input('Preco: '))
    a_data = input('Data: aaaa-mm-dd')
    cursor.execute(f'''
    INSERT INTO tb_produtos(nome, preco, dta_validade)
    VALUES('{a_nome}','{a_preco}',{a_data})
    ''')

    print('Registros inseridos: ',cursor.rowcount)
    conexao.commit()

def select():
    cursor.execute('SELECT * FROM tb_produtos')
    l_registros = cursor.fetchall()

    print('Tuplas : ', l_registros )
    print('Total de registros: ', cursor.rowcount)

def close_connection():
    cursor.close()
    conexao.close()
    print('Conexao fechada')

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()

    create_table()
    insert()
    select()
    close_connection()
    
'''
create database
create connection
create table
insert table
select
close connection
'''