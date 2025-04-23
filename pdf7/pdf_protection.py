import sys
from PyPDF2 import PdfReader, PdfWriter

def add_password_to_pdf(input_pdf, output_pdf, password):
    """
    Adds password protection to a PDF file.
    """
    try:
        # Open the input PDF
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # Copy all pages to a new PdfWriter object
        for page in reader.pages:
            writer.add_page(page)

        # Encrypt the PDF with the given password
        writer.encrypt(password)

        # Save the encrypted PDF
        with open(output_pdf, "wb") as file:
            writer.write(file)

        print(f"Password-protected PDF saved as {output_pdf}")

    except FileNotFoundError:
        print(f"Error: File '{input_pdf}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Command-line argument handling
    if len(sys.argv) != 4:
        print("Usage: python pdf_protection.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    add_password_to_pdf(input_pdf, output_pdf, password)
