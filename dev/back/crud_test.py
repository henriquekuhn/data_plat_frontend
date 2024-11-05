import pytest
from main import DatabaseConnection
import logging


# Configura o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

table_name = "test_db"

@pytest.fixture
def db_connection():
    # Cria a instância da conexão
    db = DatabaseConnection(
        host="localhost",
        database="data_plat",
        user="cafrunikuhn",
        password="admin"
    )
    
    # Estabelece a conexão antes do teste
    assert db.connect() is True, "Falha ao conectar ao banco de dados"
    
    yield db  # Isso fornece a conexão para o teste

    # Fecha a conexão após o teste
    db.close()

def test_database_connection(db_connection):
    logger.info("Testing test_database_connection...")
     # Aqui assumimos que, se a fixture `db_connection` não falhou, a conexão está ativa
    assert db_connection is not None, "A conexão com o banco de dados não foi estabelecida corretamente"


def test_create_table(db_connection):  
    logger.info("Testing test_create_table...")
    assert db_connection.create_table(table_name) is True


def test_add_column(db_connection):
    logger.info("Testing test_add_column...")
    columns_to_add = {
        "DUT": "VARCHAR(100)",
        "version": "INTEGER",
        "lot": "VARCHAR(150)"       
    }
    assert db_connection.add_columns(table_name, columns_to_add) is True


def test_data_insertion(db_connection):
    logger.info("Testing test_data_insertion...")
    columns_and_data = [
        {
        "DUT": "1",
        "version": "2",
        "lot": "nb32lot1124" 
    },
    {
        "DUT": "2",
        "version": "2",
        "lot": "nb32lot1124" 
    }
    ]

    assert db_connection.add_data(table_name, columns_and_data) is True

if __name__ == "__main__":
    pytest.main()