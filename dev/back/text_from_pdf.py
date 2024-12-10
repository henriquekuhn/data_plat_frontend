import pdfplumber
import re
import os
from main import DatabaseConnection

# Configurações para padrões e número de linhas
PATTERNS = {
    "Report Info": [12, "create_dut"],
    "Test HT criteria - ShortOpen in Default configuration": [13, "create_shortopen"],
    "Test HT criteria - Firmware Flash in Default configuration": [5, "create_firmware_flash"],
    "Test HT criteria - Interleaved in Default configuration": [22, "create_interleaved"],
    "Test HT criteria - Peripherals in Default configuration": [11, "create_peripherals"],
    "Test HT criteria - DeepSleep in Default configuration": [4, "create_deepSleep"],
    "Test Qualcomm criteria - Calibration in Default configuration": [4, "create_calibration"],
    "Test 6.2.2F - UE maximum output power in Default configuration": [10, "create_maximum_output"],
    "Test 6.5.2.1F.1 - Error vector magnitude (EVM) in Default configuration": [10, "create_evm"],
    "Test 6.5.1F - Frequency Error in Default configuration": [10, "create_frequency_error"],
    "Test 6.6.1F - Occupied bandwidth (OBW) in Default configuration": [10, "create_obw"],
    "Test 6.6.2.3F - ACLR in Default configuration": [10, "create_aclr"],
    "Test 6.6.2.1F - Spectrum Emission Mask (SEM) in Default configuration": [10, "create_sem"],
    "Test HT criteria - BLER in Default configuration": [5, "create_bler"]
}

TABLES = ["dut_register", "yield_platform"]

COLUMNS = [{
    "DUT_ID": "VARCHAR(30)",
    "OPERATOR": "VARCHAR(30)",
    "BATCH": "VARCHAR(30)",
    "START_TIME": "VARCHAR(20)",
    "TOTAL_TIME": "VARCHAR(20)",
    "TEST_PLAN": "VARCHAR(60) NOT NULL",
    "PLAT_SW_V": "VARCHAR(30) NOT NULL",
    "PLAT_HW_V": "VARCHAR(30) NOT NULL",
    "N_TEST_ITEMS": "INTEGER",
    "N_PASS_ITEMS": "INTEGER"
    },

    {
    "DUT_ID": "VARCHAR(30)",
    "TEST_TYPE": "VARCHAR(30) NOT NULL",
    "PIN_NAME": "VARCHAR(30)",
    "FLASH_STEP": "VARCHAR(30)",
    "PERIPHERAL_ID": "VARCHAR(30)",
    "SLEEP_MODE": "VARCHAR(30)",
    "CALIBRATION_ID": "VARCHAR(30)",
    "BAND": "VARCHAR(10)",
    "FREQUENCY": "VARCHAR(10)",
    "TEST_ITEM": "VARCHAR(30)",
    "DI_CHANNEL": "INTEGER",
    "CELL_LEVEL": "INTEGER",
    "LOWER_LIMT": "VARCHAR(10)",
    "UPER_LIMIT": "VARCHAR(10)",
    "RESULT": "VARCHAR(10) NOT NULL",
    "UNIT": "VARCHAR(30)",
    "JUDGEMENT": "VARCHAR(30) NOT NULL"
}]

DUT_ID = 0

def count_pdfs_in_directory(directory_path):
    pdf_number = 0
    try:
        # Percorre a árvore de diretórios
        for root, dirs, files in os.walk(directory_path):
            # Conta apenas os arquivos com extensão .pdf
            pdf_number += sum(1 for file in files if file.lower().endswith(".pdf"))
    except Exception as e:
        print(f"Erro ao contar os PDFs: {e}")
    return pdf_number

def create_dut(data, DUT_ID):
    column_data = []
    column_data.append({
        "OPERATOR": data[0].split(": ")[1],
        "DUT_ID": DUT_ID,
        "BATCH": data[2].split(": ")[1],
        "START_TIME": data[7].split(": ")[1],
        "TOTAL_TIME": data[9].split(": ")[1],
        "TEST_PLAN": data[3].split(": ")[1].strip("[]'"),
        "PLAT_SW_V": data[4].split(": ")[1],
        "PLAT_HW_V": data[5].split(": ")[1],
        "N_TEST_ITEMS": data[12].split(": ")[1],
        "N_PASS_ITEMS": data[10].split(": ")[1]
       })
    db.add_data(TABLES[0], column_data)


def create_shortopen(data, DUT_ID):
    column_data = []
    pattern = r"^(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"

    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "short open",
                "PIN_NAME": match.group(1),
                "LOWER_LIMT": match.group(2),
                "UPER_LIMIT": match.group(3),
                "RESULT": 1,
                "UNIT": "kohm",
                "JUDGEMENT": match.group(6)
            })
    #for row in column_data:
    #    print(row)    
    db.add_data(TABLES[1], column_data)

def create_firmware_flash(data, DUT_ID):
    column_data = []

    # Regex para capturar as colunas corretamente
    pattern = r"^(.*?)\s+(-|[\d\.]+)\s+(-|[\d\.]+)\s+([\w\.]+)\s+([\w\.-]+)\s+([\w]+)$"

    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "firmware flash",
                "FLASH_STEP": match.group(1),  # Primeira coluna (nomes com espaços)
                "RESULT": 0 if match.group(6) == 'FAIL' else 1,
                "JUDGEMENT": match.group(6)   # Última coluna (Judgement)
            })

    #for row in column_data
    #    print(row)
    #print(column_data)
    db.add_data(TABLES[1], column_data)    

def create_interleaved(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "interleaved",
                "PIN_NAME": match.group(1),
                "LOWER_LIMT":  match.group(2),
                "UPER_LIMIT": match.group(3),
                "RESULT": match.group(4),
                "JUDGEMENT": match.group(6)
                })
    #for row in column_data:
    #    print(row)    
    #print(column_data)
    db.add_data(TABLES[1], column_data) 

def create_peripherals(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "peripherals",
                "PIN_NAME": match.group(1),
                "RESULT": 0 if match.group(6) == 'FAIL' else 1,
                "JUDGEMENT": match.group(6)
            })
    #for row in column_data:
    #    print(row)    
    #print(column_data)
    db.add_data(TABLES[1], column_data)

def create_deepSleep(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "deepSleep",
                "SLEEP_MODE": match.group(1),
                "LOWER_LIMT": match.group(2),
                "UPER_LIMIT": match.group(3),
                "RESULT": match.group(4),
                "UNIT": "uA",
                "JUDGEMENT": match.group(6)
            })
    #for row in column_data:
    #    print(row)    
    #print(column_data)
    db.add_data(TABLES[1], column_data)


def create_calibration(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "calibration",
                "CALIBRATION_ID": match.group(1),
                "RESULT": 0 if match.group(6) == 'FAIL' else 1,
                "JUDGEMENT": match.group(6)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)
    
def create_maximum_output(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "maximum_output",
                "BAND": match.group(1),
                "FREQUENCY": match.group(2),
                "TEST_ITEM": match.group(3),
                "LOWER_LIMT": match.group(4),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "dBm",
                "JUDGEMENT": match.group(8)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)

def create_evm(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "evm",
                "BAND": match.group(1),
                "FREQUENCY": match.group(2),
                "TEST_ITEM": match.group(3),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "%",
                "JUDGEMENT": match.group(8)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)

def create_frequency_error(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "frequency error",
                "BAND": match.group(1),
                "FREQUENCY": match.group(2),
                "TEST_ITEM": match.group(3),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "Hz",
                "JUDGEMENT": match.group(8)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)

def create_obw(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "obw",
                "BAND": match.group(1),
                "FREQUENCY": match.group(2),
                "TEST_ITEM": match.group(3),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "Hz",
                "JUDGEMENT": match.group(8)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)

def create_aclr(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "aclr",
                "BAND": match.group(1),
                "FREQUENCY": match.group(2),
                "TEST_ITEM": match.group(3),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "dBc",
                "JUDGEMENT": match.group(8)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)

def create_sem(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "sem",
                "BAND": match.group(1),
                "FREQUENCY": match.group(2),
                "TEST_ITEM": match.group(3),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "%",
                "JUDGEMENT": match.group(8)
            })
    #for row in column_data:
    #    print(row)
    db.add_data(TABLES[1], column_data)

def create_bler(data, DUT_ID):
    column_data = []
    pattern = r"^([A-Za-z0-9\s\[\]\-]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
    for line in data[1:]:
        match = re.match(pattern, line)
        if match:
            column_data.append({
                "DUT_ID": DUT_ID,
                "TEST_TYPE": "bler",
                "BAND": match.group(1),
                "DI_CHANNEL": match.group(2),
                "CELL_LEVEL": match.group(3),
                "UPER_LIMIT": match.group(5),
                "RESULT": match.group(6),
                "UNIT": "%",
                "JUDGEMENT": match.group(8)
            })
        #for row in column_data:
        #    print(row)
        db.add_data(TABLES[1], column_data)

def find_and_copy_lines(pdf_path, patterns):
    results = {pattern: [] for pattern in patterns}  # Dicionário para armazenar resultados
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split("\n")  # Divide o texto da página em linhas

            # Para cada padrão, procura e armazena as linhas desejadas
            for pattern, num_lines in patterns.items():
                normalized_pattern = re.compile(re.escape(pattern), re.IGNORECASE)  # Ignora maiúsculas/minúsculas
                for i, line in enumerate(lines):
                    normalized_line = line.strip().lower()  # Normaliza a linha para evitar erros de espaços
                    if normalized_pattern.search(normalized_line):
                        # Armazena a linha encontrada e as próximas `num_lines` linhas
                        results[pattern].extend(lines[i + 1:i + num_lines[0] + 2])
                        break  # Sai do loop ao encontrar o padrão para evitar duplicação

    return results

def process_all_pdfs_in_directory(directory_path, patterns):
    global DUT_ID
    # Conta os PDFs na árvore de pastas
    pdf_number = count_pdfs_in_directory(directory_path)
    pdf_count = 0
    all_results = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:

            pdf_count += 1
            if file.lower().endswith(".pdf"):
                DUT_ID += 1
                pdf_path = os.path.join(root, file)
                print(f"Processing: {pdf_count} of {pdf_number} files.")
                results = find_and_copy_lines(pdf_path, patterns)
                all_results[pdf_path] = results  # Armazena o resultado de cada PDF
                # Imprime as linhas encontradas para cada padrão no PDF atual
                for pattern, lines in results.items():
                    if lines:
                        
                        func_name = patterns[pattern][1]
                        globals()[func_name](lines, DUT_ID)                       

                        #print(f"\nPadrao: {pattern} em {pdf_path}")
                        for line in lines:
                            line_split = line.split(" ")
                            #print(line_split)
                            #print(line)
                        #print("\n" + "="*40 + "\n")
                    else:
                        pass
                        #print(f"\nNenhuma linha encontrada para o padrão '{pattern}' em {pdf_path}\n")
    return all_results

def create_tables(tables, columns):
    for table in tables:
        db.create_table(table)
        db.add_columns(table, columns[tables.index(table)])

db = DatabaseConnection(
        host="localhost",
        database="data_plat",
        user="cafrunikuhn",
        password="admin"
    )

db.connect()
create_tables(TABLES, COLUMNS)

directory_path = "C:\\Users\\adm_cafrunikuhn\\Desktop\\Henrique\\Repositories\\data_plat\\Batchs"
process_all_pdfs_in_directory(directory_path, PATTERNS)
