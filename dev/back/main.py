import psycopg2
from psycopg2 import sql
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self, host, database, user, password):
        '''Initialize the database connection parameters.'''
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None  # Initialize the cursor as None

    def connect(self):
        """Establishes the connection to the database and checks if the connection is active."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Successful connection to the database.")

            # Check if the connection is active by executing a simple command
            self.cursor = self.connection.cursor()  # Initialize the cursor here
            self.cursor.execute("SELECT 1;")
            result = self.cursor.fetchone()
            if result:
                print("The connection is active and working.")
                return True
            else:
                print("The connection was established, but it could not be verified.")
                return False
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            logger.info(e)
            return False

    def close(self):
        """Closes the connection to the database."""
        if self.connection:
            self.connection.close()
            print("Connection to the database closed.")

    def create_table(self, table_name):
        '''Creates a new table in the database.'''
        try:
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    ID SERIAL PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error creating the table '{table_name}': {e}")
            self.connection.rollback()
            logger.info(e)
            return False

    def add_columns(self, table_name, columns):
        """
        Adds columns to an existing table in the database.

        :param table_name: Name of the table.
        :param columns: Dictionary where the key is the column name and the value is the column type (e.g., "column_name": "VARCHAR(100)").
        :return: True if the columns were added successfully, otherwise False.
        """
        try:
            add_column_queries = ", ".join([f"ADD COLUMN {col_name} {col_type}" for col_name, col_type in columns.items()])

            # Complete command to add the columns
            query = f"ALTER TABLE {table_name} {add_column_queries};"

            # Execute the command
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Columns {', '.join(columns.keys())} added to table '{table_name}' successfully.")
            return True

        except Exception as e:
            print(f"Error adding columns to table '{table_name}': {e}")
            self.connection.rollback()
            logger.info(e)
            return False

    def add_data(self, table_name, column_data):
        """
        Adds data to an existing column in the database table.

        :param table_name: Name of the table.
        :param column_data: List of dictionaries, where each dictionary represents a row with columns as keys and values as data (e.g., "column_name": "data").
        :return: True if the data was added successfully, otherwise False.
        """
        try:
            if not column_data:
                logger.info("No data to insert.")
                return False

            # Extract columns and values from the dictionary
            columns = ", ".join(column_data[0].keys())
            values = ", ".join([f"%({key})s" for key in column_data[0].keys()])

            # Construct the query with placeholders to avoid SQL injection
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

            self.cursor.executemany(query, column_data)
            self.connection.commit()

            return True

        except Exception as e:
            print(f"Error inserting data into table '{table_name}': {e}")
            self.connection.rollback()
            logger.info(e)
            return False

    def delete_data(self, table_name, reference, data):
        '''Deletes data from the specified table based on the reference condition.'''
        try:
            query = f"DELETE FROM {table_name} WHERE {reference} = %s"
            self.cursor.execute(query, (data))  # Use parameterized query to avoid SQL injection
            self.connection.commit()
            return True
        
        except Exception as e:
            self.connection.rollback()
            logger.info(e)
            return False


    def update_data(self, table_name, update_column, new_value, reference_column_and_value):
        """
        Atualiza dados na tabela especificada com base em uma condição de referência.

        :param table_name: Nome da tabela.
        :param update_column: Coluna a ser atualizada.
        :param new_value: Novo valor para a coluna.
        :param reference_column_and_value: Dicionario com lista de coluna e seus valores correspondentes.
        :return: True se a atualização for bem-sucedida, False em caso de erro.
        """
        try:
            conditions = " AND ".join([f"{ref_col} = %s" for ref_col in reference_column_and_value.keys()])
            parameters = (new_value, *reference_column_and_value.values())
            query = f"UPDATE {table_name} SET {update_column} = %s WHERE {conditions}"

            self.cursor.execute(query, parameters)
            self.connection.commit()
            return True
    
        except Exception as e:
            self.connection.rollback()  # Desfaz a operação em caso de erro
            logger.info(f"Erro ao atualizar dados: {e}")
            
            return False