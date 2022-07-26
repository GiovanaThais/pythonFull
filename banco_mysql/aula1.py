import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             database='pythonfull',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    
    with connection.cursor() as cursor:
        # Create a new record
    
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    def criarTabela(nomeTabela):
        try:
            with connection.cursor() as cursor:
                #criando tabela
                cursor.execute(f"create table {nomeTabela}")
            print("tabela criada com sucesso")

            connection.commit()
        except Exception as e:
            print(f'ocorreu um erro {e}')

    def removerTabela(nomeTabela):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"drop table {nomeTabela}")
            print("tabela removida com sucesso")
        except Exception as e:
            print(f"ocorreu um erro ao remover {e}")

    def inserirNaTabela(nome):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO teste values ('{nome}')")
            print("valor inserido com sucesso")
        except Exception as e:
            print(f"ocorreu um erro ao remover {e}")

    def SelectTabela():
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM teste")
                result = cursor.fetchall() #fetchall para pegar todos os elementos ( todas as linhas do banco)
        except Exception as e:
            print(f"ocorreu um erro ao selecionar {e}")

    def atualizarTabela():
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE teste SET nome= 'Maria' WHERE nome = 'Maria")
                print("atualizado com sucesso")
        except Exception as e:
            print(f"ocorreu um erro ao atualizar {e}")

    def deletarTabela():
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM teste WHERE nome = 'Maria")
                print("remoção feita com sucesso")
        except Exception as e:
            print(f"ocorreu um erro ao deletar {e}")

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone() # fetchone para pegar apenas uma linha do banco
        print(result)

