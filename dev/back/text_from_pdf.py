import PyPDF2


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    return text

pdf_path = "C:\\Users\\adm_cafrunikuhn\\Desktop\\Henrique\\Repositories\\data_plat\\Batchs\\NBITT07-06-000-RETEST\\NBITT07-06-000-RETEST_FAIL_2024-10-21_17-13-42.pdf"
print(extract_text_from_pdf(pdf_path))