import pytest
from main import DatabaseConnection
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

table_name = "test_db"

@pytest.fixture
def db_connection():
    '''Fixture to create a database connection before each test.'''
    # Create an instance of the connection
    db = DatabaseConnection(
        host="localhost",
        database="data_plat",
        user="cafrunikuhn",
        password="admin"
    )
    
    # Establish the connection before the test
    assert db.connect() is True, "Failed to connect to the database"
    
    yield db  # This provides the connection for the test

    # Close the connection after the test
    db.close()

def test_database_connection(db_connection):
    logger.info("Testing test_database_connection...")
    # Here we assume that if the `db_connection` fixture did not fail, the connection is active
    assert db_connection is not None, "The connection to the database was not established correctly"

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

def test_delete_by_dut(db_connection):
    logger.info("Testing test_delete_by_id...")
    column = "DUT"
    data = "2"

    assert db_connection.delete_data(table_name, column, data) is True

def test_delete_by_id(db_connection):
    logger.info("Testing test_delete_by_id...")
    column = "id"
    data = "1"

    assert db_connection.delete_data(table_name, column, data) is True

def test_update_by_id(db_connection):
    logger.info("Testing test_update_by_dut...")    
    reference_column_and_value = {
        "id": "45"
    }
    update_column = "DUT"
    new_data = "100"

    assert db_connection.update_data(table_name, update_column, new_data, reference_column_and_value) is True


def test_update_by_dut(db_connection):
    logger.info("Testing test_update_by_dut...")
    reference_column_and_value = {
        "DUT": "1"
    }
    update_column = "LOT"
    new_data = "lote_atualizado_"

    assert db_connection.update_data(table_name, update_column, new_data, reference_column_and_value) is True


def test_update_by_specific_condition(db_connection):
    logger.info("Testing test_update_by_dut...")
    reference_column_and_value = {
        "DUT": "100",
        "lot": "lote_atualizado"
    }
    update_column = "version"
    new_data = "40"

    assert db_connection.update_data(table_name, update_column, new_data, reference_column_and_value) is True

if __name__ == "__main__":
    pytest.main()
