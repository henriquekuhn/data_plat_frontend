import logging


# Configura o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_data(db_conn, table_name):
    try:
        query = f"SELECT * FROM {table_name};"
        db_conn.cursor.execute(query)
        results = db_conn.cursor.fetchall()
        return results
    except Exception as e:
        logger.info(f"Erro ao ler dados da tabela '{table_name}': {e}")
        return None
