from MyCRUD import ConectarDB

# Instanciando a classe e iniciando conexão com o banco
banco = ConectarDB()

# criando tabela

banco.criar_tabela()

# dados
dados = [('Thomaz',19544706742), ('Edson',73753009739), ('Luzia', 73750821348)]

# Inserir um registro na tabela

banco.inserir_registros(dados)

# Consultar um registro na tabela através do ID

print(banco.consultar_registro(2))

# consultar todos os registros na tabela

print(banco.consultar_registros())

# Alterar registro na tabela

banco.alterar_registro('Bruna',19544706749, 2)
print(banco.consultar_registro(2))

# Remover registro na tabela
banco.remover_registro(2)
