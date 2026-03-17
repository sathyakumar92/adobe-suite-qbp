import PyPDF2
import os

def extract_text_from_pdf(pdf_path, output_txt_path):
    """
    Extracts text from a PDF file and saves it to a text file.
    
    :param pdf_path: Path to the PDF file to be read.
    :param output_txt_path: Path to the output text file.
    :raises FileNotFoundError: If the PDF file does not exist.
    :raises ValueError: If the file is not a PDF.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    
    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError(f"The file {pdf_path} is not a PDF file.")
    
    try:
        with open(pdf_path, 'rb') as file:
            try:
                reader = PyPDF2.PdfReader(file)
            except PyPDF2.errors.PdfReadError as e:
                raise ValueError(f"Invalid or corrupted PDF file: {e}")
            
            text = []
            for page in reader.pages:
                text.append(page.extract_text() or "")
            
            # Join all the extracted text
            extracted_text = "\n".join(text)
        
        # Write to the output file
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)
        
        print(f"Text extracted successfully and saved to {output_txt_path}")
    
    except Exception as e:
        print(f"An error occurred while processing the PDF: {e}")

# TODO: Add support for password-protected PDFs
# TODO: Implement logging instead of print statements for better traceability
# TODO: Enhance text extraction logic for better formatting and handling of images/graphs

if __name__ == "__main__":
    # Example usage (this part can be moved to main.py)
    try:
        extract_text_from_pdf('sample.pdf', 'output.txt')
    except Exception as e:
        print(f"Error: {e}")
