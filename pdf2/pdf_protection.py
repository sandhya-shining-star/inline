import PyPDF2
import sys

# Function to create a password-protected PDF
def create_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        # Open the input PDF file in read-binary mode
        with open(input_pdf, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)  # Create a PdfReader object
            pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object
            
            # Loop through all the pages in the PDF
            for page_number in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_number])  # Add pages to the writer
            
            # Encrypt the PDF with the provided password
            pdf_writer.encrypt(password)
            
            # Write the encrypted PDF to the output file
            with open(output_pdf, "wb") as encrypted_file:
                pdf_writer.write(encrypted_file)
        
        print(f"[+] The file '{output_pdf}' has been created and is password-protected.")
    
    except FileNotFoundError:
        print(f"[!] Error: The file '{input_pdf}' was not found. Please check the file path.")
    except PyPDF2.errors.PdfReadError:
        print(f"[!] Error: Unable to read '{input_pdf}'. The file may be corrupted or not a valid PDF.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

# Main function to handle command-line arguments
def main():
    if len(sys.argv) != 4:  # Check for proper usage
        print("Usage: python pdf_protection.py <input_pdf> <output_pdf> <password>")
        return
    
    input_pdf = sys.argv[1]  # First argument: input PDF file
    output_pdf = sys.argv[2]  # Second argument: output PDF file
    password = sys.argv[3]  # Third argument: password for the output PDF
    
    # Call the function to create the password-protected PDF
    create_password_protected_pdf(input_pdf, output_pdf, password)

# Entry point
if __name__ == "__main__":
    main()
