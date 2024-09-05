import os
from PyPDF2 import PdfReader

def load_pdfs(pdf_folder):
    documents = []
    filenames = []
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            file_path = os.path.join(pdf_folder, pdf_file)
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                documents.append(text)
                filenames.append(pdf_file)
    return documents, filenames