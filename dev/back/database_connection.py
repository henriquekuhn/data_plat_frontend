import psycopg2
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
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o banco de dados e inicializa o cursor."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida ao banco de dados.")
            return True
        except Exception as e:
            logger.info(f"Erro ao conectar ao banco de dados: {e}")
            return False

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Conexão com o banco de dados fechada.")
