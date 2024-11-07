import logging


# Configura o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_table(db_conn, table_name):
    if db_conn.connection is None:
        logger.info("Conexão não estabelecida. Impossível criar a tabela.")
        return False
    try:
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        db_conn.cursor.execute(create_table_query)
        db_conn.connection.commit()
        print(f"Tabela '{table_name}' criada com sucesso.")
        return True
    except Exception as e:
        db_conn.connection.rollback()
        logger.info(f"Erro ao criar a tabela '{table_name}': {e}")
        return False
    

def add_columns(db_conn, table_name, columns):
    try:
        add_column_queries = ", ".join([f"ADD COLUMN {col} {typ}" for col, typ in columns.items()])
        query = f"ALTER TABLE {table_name} {add_column_queries};"
        db_conn.cursor.execute(query)
        db_conn.connection.commit()
        print(f"Colunas {', '.join(columns.keys())} adicionadas à tabela '{table_name}' com sucesso.")
        return True
    except Exception as e:
        db_conn.connection.rollback()
        logger.info(f"Erro ao adicionar colunas na tabela '{table_name}': {e}")
        return False