import psycopg2
from psycopg2 import sql
import logging


# Configura o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None  # Inicializando o cursor como None

    def connect(self):
        """Estabelece a conexão com o banco de dados e verifica se a conexão está ativa."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexão bem-sucedida ao banco de dados.")

            # Verifica se a conexão está ativa executando um comando simples
            self.cursor = self.connection.cursor()  # Inicializa o cursor aqui
            self.cursor.execute("SELECT 1;")
            result = self.cursor.fetchone()
            if result:
                print("A conexão está ativa e funcionando.")
                return True
            else:
                print("A conexão foi estabelecida, mas não foi possível verificar.")
                return False
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            logger.info(e)
            return False

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados fechada.")


    def create_table(self, table_name):
        try:
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            return True
        
        except Exception as e:
            print(f"Erro ao criar a tabela '{table_name}': {e}")
            self.connection.rollback()
            logger.info(e)
            return False

    def add_columns(self, table_name, columns):
        """
        Adiciona colunas a uma tabela existente no banco de dados.

        :param table_name: Nome da tabela.
        :param columns: Dicionário onde a chave é o nome da coluna e o valor é o tipo da coluna (e.g., "column_name": "VARCHAR(100)").
        :return: True se as colunas foram adicionadas com sucesso, caso contrário False.
        """

        try:
            add_column_queries = ", ".join([f"ADD COLUMN {col_name} {col_type}" for col_name, col_type in columns.items()])

        # Comando completo para adicionar as colunas
            query = f"ALTER TABLE {table_name} {add_column_queries};"

            # Executa o comando
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Colunas {', '.join(columns.keys())} adicionadas à tabela '{table_name}' com sucesso.")
            return True

        except Exception as e:
            print(f"Erro ao adicionar colunas na tabela '{table_name}': {e}")
            self.connection.rollback()
            logger.info(e)
            return False

    
    def add_data(self, table_name, column_data):
        """
        Adiciona dado a uma coluna existente na tabela de banco de dados.

        :param table_name: Nome da tabela.
        :param column_data: Lista de dicionários, onde cada dicionário representa uma linha com colunas como chave e valores como valor. (e.g., "column_name": "data").
        :return: True se as colunas foram adicionadas com sucesso, caso contrário False.
        """

        try:

            if not column_data:
                logger.info("Nenhum dado para inserir.")
                return False

            # Extrai as colunas e os valores do dicionário
            columns = ", ".join(column_data[0].keys())
            values = ", ".join([f"%({key})s" for key in column_data[0].keys()])

            # Construção da query com placeholders para evitar SQL injection
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

            self.cursor.executemany(query, column_data)
            self.connection.commit()

            return True

        except Exception as e:
            print(f"Erro ao inserir dados na tabela '{table_name}': {e}")
            self.connection.rollback()
            logger.info(e)
            return False