################################################ Word extractor ############################################################
from docx import Document
def extract_text_from_word(path):
    text = ""
    
    doc = Document(path)
    for para in doc.paragraphs:
        text += para.text
    return text

text = extract_text_from_word("D:/Work/Codes/git repository/Python/Python Project/Python.docx")
print(text)


################################################ PDF extractor ############################################################
from PyPDF2 import PdfReader
def get_pdf_text(pdf_docs):
    '''
    Extract text from PDF documents
    Args: pdf_docs: List of PDF file paths
    return: Text extracted from PDFs

    Example:
    pdf_docs = ["file1.pdf", "file2.pdf"]
    text = get_pdf_text(pdf_docs)
    '''
    
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


pdf_docs = ["D:/Work/Codes/git repository/Python/Python Project/PDF/12 Rules to Learn to Code [2nd Edition] 2022.pdf","D:/Work/Codes/git repository/Python/Python Project/PDF/Al Sweigart - Automate The Boring Stuff with Python 2019.pdf"]
text = get_pdf_text(pdf_docs[:200])

# Print first 500 characters
print(text)  

################################################ trim path ############################################################
def trim_path(path):
    '''
    Trim leading and trailing slashes from a path
    Args: path: Input path
    return: Trimmed path
    '''
    if path:
        return path.rstrip('/').lstrip('/')
    return path

    trim_path('/C:/Python/trim_path//')  
    # Output: 'C:/Python/trim_path'