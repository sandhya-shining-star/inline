# Read a PDF and print page count 
import PyPDF2 
pdf_file = "sample.pdf"  # Replace with a real PDF 
try: 
    with open(pdf_file, "rb") as f: 
        pdf_reader = PyPDF2.PdfReader(f) 
        page_count = len(pdf_reader.pages) 
        print(f"{pdf_file} has {page_count} pages") 
except FileNotFoundError: 
    print(f"{pdf_file} not found")