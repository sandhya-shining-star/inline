# Test opening a PDF with pikepdf 
import pikepdf 
pdf_file = "protected.pdf"  # Replace with a real protected PDF 
password = "wrongpass"  # Replace with a test password 
try: 
    with pikepdf.open(pdf_file, password=password) as pdf: 
        print(f"Opened {pdf_file} with {len(pdf.pages)} pages") 
except pikepdf._core.PasswordError: 
    print(f"Password '{password}' failed for {pdf_file}")