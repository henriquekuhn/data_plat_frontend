from sqlalchemy import create_engine, MetaData, Table, select, func

def list_column_values(engine, table, column_name):
    """
    Lista os valores distintos de uma coluna para um filtro.

    :param engine: Engine SQLAlchemy.
    :param table: Objeto da tabela SQLAlchemy.
    :param column_name: Nome da coluna para filtrar.
    :return: Lista de valores distintos da coluna.
    """
    with engine.connect() as connection:
        query = select(table.c[column_name]).distinct()  # Corrigido para passar a coluna diretamente
        result = connection.execute(query)
        return [row[0] for row in result]

def list_filter_options_and_select():
    """
    Exibe as opções de filtro e permite ao usuário selecionar um filtro.

    :return: Nome do filtro selecionado (batch).
    """
    print("\nEscolha o filtro:")
    print("1. Filtrar por batch")
    print("2. Ver todos os dados (sem filtro)")

    try:
        filter_choice = int(input("Digite o número do filtro desejado: ")) - 1
        if filter_choice == 0:
            return "batch"
        elif filter_choice == 1:
            return None  # Ver todos os dados
        else:
            raise ValueError("Escolha inválida.")
    except ValueError as e:
        print(f"Erro: {e}")
        return None

def query_data(engine, dut_register_table, yield_platform_table, filter_column=None, filter_value=None):
    """
    Realiza uma consulta na tabela yield_platform com base no filtro aplicado na tabela dut_register.

    :param engine: Engine SQLAlchemy.
    :param dut_register_table: Tabela dut_register.
    :param yield_platform_table: Tabela yield_platform.
    :param filter_column: Nome da coluna para filtrar na tabela dut_register.
    :param filter_value: Valor para o filtro.
    """
    with engine.connect() as connection:
        if filter_column and filter_value:
            # Consulta na tabela dut_register com o filtro especificado
            dut_register_query = select(dut_register_table).where(dut_register_table.c[filter_column] == filter_value)
            dut_register_result = connection.execute(dut_register_query)
            dut_register_rows = dut_register_result.fetchall()

            # Obtém os ids correspondentes de dut_register
            dut_ids = [row.dut_id for row in dut_register_rows]

            # Consulta na tabela yield_platform usando os dut_ids da tabela dut_register
            if dut_ids:
                yield_platform_query = select(yield_platform_table).where(yield_platform_table.c.dut_id.in_(dut_ids))
                yield_platform_result = connection.execute(yield_platform_query)
                yield_platform_rows = yield_platform_result.fetchall()

                print(f"Resultados ({len(yield_platform_rows)} registros encontrados na yield_platform):")
                for row in yield_platform_rows:
                    print(row)
            else:
                print("Nenhum registro encontrado na tabela dut_register para o filtro especificado.")
        else:
            # Se não houver filtro, retorna todos os dados da tabela yield_platform
            yield_platform_query = select(yield_platform_table)
            yield_platform_result = connection.execute(yield_platform_query)
            yield_platform_rows = yield_platform_result.fetchall()

            print(f"Resultados ({len(yield_platform_rows)} registros encontrados na yield_platform):")
            for row in yield_platform_rows:
                print(row)

if __name__ == "__main__":
    # Configuração da conexão ao banco de dados
    DATABASE_URL = "postgresql+psycopg2://cafrunikuhn:admin@localhost/data_plat"
    engine = create_engine(DATABASE_URL)

    # Reflete as tabelas existentes no banco de dados
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Obtém as tabelas de dut_register e yield_platform
    dut_register_table = metadata.tables['dut_register']
    yield_platform_table = metadata.tables['yield_platform']

    # Escolhe o filtro
    filter_type = list_filter_options_and_select()

    if filter_type:
        if filter_type == "batch":
            # Lista os valores distintos de 'batch' na tabela dut_register
            batches = list_column_values(engine, dut_register_table, "batch")
            print("Valores de 'batch' disponíveis:")
            for idx, batch in enumerate(batches, start=1):
                print(f"{idx}. {batch}")
            batch_choice = int(input("Escolha o número do batch para filtrar: ")) - 1
            if 0 <= batch_choice < len(batches):
                filter_value = batches[batch_choice]
                # Realiza a consulta e imprime os resultados da yield_platform
                query_data(engine, dut_register_table, yield_platform_table, "batch", filter_value)
        else:
            # Se não selecionar filtro, mostra todos os dados da yield_platform
            query_data(engine, dut_register_table, yield_platform_table)
    else:
        print("Nenhum filtro foi selecionado.")
