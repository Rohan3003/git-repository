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
