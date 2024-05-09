import sqlite3
import os

def conectar_db():

        con = None
        cursor = None

        try:
                con = sqlite3.connect("db.sqlite")
                cursor = con.cursor()
        except:
                print('Erro na conexão com o Banco de Dados')

        return con, cursor

#comn = sqlite3.connect("db.sqlite")
#cursor = comn.cursor()


#LIMPANDO O TERMINAL
def limpar_tela():

        return os.system('cls')

#CRIANDO A TABELA CARROS SE ELA NÃO EXISTIR
def criar_tcarros():

        con, cursor = conectar_db()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS carros(
                            
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT NOT NULL,
                            ano VARCHAR(9) NOT NULL,
                            qtd_portas INTEGER NOT NULL,
                            potencia INTEGER NOT NULL
                        )
                       """)
        con.close()

#ADICIONANDO INFORMAÇÕES NA TABELA CARS
def add_info_tcarros():
        
        print(f'{'-'*10} TELA DE CADASTRO {'-'*10}\n')
        tipo = input("Informe o tipo do carro: ").upper()
        ano = input("Informe o ano do carro: ")
        qtd_portas = int(input("Informe a quantidade de portas do carro: "))
        potencia = int(input("Informe a potencia do carro: "))

        con, cursor = conectar_db()

        cursor.execute("""

                        INSERT INTO carros(tipo, ano, qtd_portas, potencia) VALUES(?, ?, ?, ?)
                       """, (tipo, ano, qtd_portas, potencia))
        
        con.commit()
        print('\nCarro cadastrado com sucesso!\n')

        con.close()

#LISTANDO TODOS OS CARROS NO BANCO DE DADOS
def listar_carros():
        
        con, cursor = conectar_db()

        carros = cursor.execute("""
                                
                                SELECT * FROM carros
                              """).fetchall()
        
        
        print(f'{'-'*30} CARROS CADASTRADOS {'-'*30}\n')
        for carro in carros:

                print(f'ID: {carro[0]}    TIPO: {carro[1]}    ANO: {carro[2]}    PORTAS: {carro[3]}    POTENCIA: {carro[4]} CV')

        con.close()

#BUSCANDO UM CARRO PELO ID
def buscando_carro():

        print(f'{'-'*10} TELA DE BUSCA {'-'*10}\n')
        id = input('Informe o ID do carro: ')

        con, cursor = conectar_db()

        carro = cursor.execute("""

                        SELECT * FROM carros WHERE "id" = ?
                        """, (id)).fetchone()
        
        print(f'\n{'-'*10} RESULTADO DA BUSCA {'-'*10}\n')
        print(f'ID: {carro[0]}    TIPO: {carro[1]}    ANO: {carro[2]}    PORTAS: {carro[3]}    POTENCIA: {carro[4]} CV\n')

        con.close()

#MENU
def menu():

        limpar_tela()
        print(f'\n{'-'*10} MENU {'-'*10}')
        print('1 - Cadastrar Carro')
        print('2 - Listar Carros')
        print('3 - Buscar Carro')
        print('0 - Sair\n')

        escolha = int(input('Informe o número correspondente a opção desejada: '))
        return escolha

def retornar_menu():

        retorna_menu = int(input('\nDeseja retornar ao menu? (1 - SIM; 2 - NÂO): '))
        
        return 1 if retorna_menu == 1 else 2

        

        