class ConectarDB:

    def __init__(self):
        
        import sqlite3 as sl

        # Conectando no Banco 

        # Conectando...
        self.conexao = sl.connect('moleza.sqlite3')
        print('Conexão feita com sucesso')

        # Cursor: é um interador que permite navegar e manipular os registros do bd.
        self.cursor = self.conexao.cursor()
    
    
    def fecharDB(self): 
        self.conexao.close()


    def criar_tabela(self):
            # Cria a tabela caso ela não exista
            # Execute: lê e executa comandos SQL puro diretamente no bd.
            try:
               sql = """
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf VARCHAR(11) NOT NULL

                );

                """
            except:
                print('Falha ao criar Tabela')
            else:
                self.cursor.execute(sql)
                print('Tabela criada com sucesso!!!')


    def inserir_registros(self, lista=list):
        # Adiciona novas linhas na tabela 
        # Vamos passar diversos dados através de uma lista com tuplas 
            try:
                self.cursor.executemany("""INSERT INTO pessoas (nome, cpf) VALUES(?, ?)""", lista)    
            except:
                print('Falha ao inserir registro')
                print('Revertendo operação')
                # rollback desfaz a operação
                self.conexao.rollback()
            else:
                # commit registra a operação/transação no banco.
                self.conexao.commit()
                print('Registro inserido com sucesso')


    def consultar_registro(self, rowid):
        # rowid (int): id do usuário o qual deseja consultar
        # utilizando o return para retornar uma tupla com os dados
        # caso naõ encontre, o valor retornado é o none 
        try:
            registro = self.cursor.execute('''SELECT * FROM pessoas WHERE rowid=?''', (rowid,)).fetchone()
        except:
            print('Falha ao consultar registro')
        else:
            return registro

    def consultar_registros(self):
        sql = """

        SELECT * FROM pessoas;

        """
        resultado = self.cursor.execute(sql).fetchall()
        return resultado


    def alterar_registro(self, nome, cpf, id):
        # nome que se deseja alterar (string)
        # cpf que se deseja alterar (int)
        
        sql = """
            UPDATE pessoas
            SET nome =?, cpf =?
            WHERE id =?;
        """
        self.cursor.execute(sql, (nome, cpf, id))
        self.conexao.commit()
        print('Registro alterado com sucesso')

    def remover_registro(self, id):
        sql = """
            DELETE FROM PESSOAS WHERE id=?
        """
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
        print('Registro removido com sucesso')



