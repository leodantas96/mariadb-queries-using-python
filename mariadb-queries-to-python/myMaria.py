# Importamos o mysql.connector para nos ligarmos à nossa BD na mariadb
# Importamos o modulo tabulate (pip install tabulate) que nos permitirá gerar tabelas com as queries
# Importamos o myModule para podermos importar o cabeçalho e apagar a consola 
import mysql.connector as mariadb
from tabulate import tabulate
from myModule import *

# criamos a variavel global de conexão à base de dados que é uma lista que permite armazenar diferentes tipos de dados
conn = " "

# Aqui definimos a função "conexão à base de dados"
# invocamos a variavél global de conexão à base de dados
# dentro dessa variavel, criamos uma lista com os campos que nos permitem fazer a ligação à mariadb
# se todas as informações estiverem corretas, aparecerá a mensagem de ligação efetuada com sucesso
# caso contrário, aparece o parâmetro específico onde se encontra o erro
# se a função correr sem erros, devolve 1; caso contrário devolve 0
def connectionDB():
    try:
        global conn
        conn = mariadb.connect(
            user="enterprise",
            password="enterprise", 
            host="127.0.0.1", 
            port=3307, 
            database="datawarehouse"
        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return (1)
    
    return "Ligação com sucesso! Bem-vindo :)"


# criamos a função de fim de sessão de ligação à base de dados
# invocamos a variavél global de conexão à base de dados
# fechamos a sessão e returnamos a string de fecho de sessão
def disconnectionDB():
    global conn
    conn.close
    return "Ligação terminada! Até à próxima :("


# Criamos a função selecttable que recebe 2 parâmetros
# s - query que vamos executar
# headers - títulos dos cabeçalhos da respetiva query
def selecttable(s, headers):
    global conn
    # existe um cursor de abertura e de fecho
    # o cursor.execute vai executar a query escolhida
    # o cursor.fetchall retorna todas as linhas de uma query
    cursor = conn.cursor()
    try:
        cursor.execute( s )
        result = cursor.fetchall()
        
        # O módulo tabulate imprime dados em formato de tabela em Python
        # numalign - alinhar o conteúdo no lado indicado (left, right, center)
        # floatfmt - devolve floats com 0 casas decimais
        # fancy-grid é para colocar a grelha na tabela
        print(tabulate(result, headers, numalign="center", floatfmt=".0f", tablefmt="fancy_grid"))
        
        cursor.close()

    # se se verificar algum erro, devolve o respetivo erro em string e retorna o inteiro 0
    except mariadb.Error as e:
        myError = "Error is " + str(e.args[0]) + " " + str(e.args[1])
        print(myError)

    return (1)