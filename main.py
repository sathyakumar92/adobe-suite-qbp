import argparse
import os
import PyPDF2

def extract_text_from_pdf(pdf_path, output_path):
    """Extract text from PDF and save to file."""
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Extract text from PDF files and save to a text file.')
    parser.add_argument('pdf_file', type=str, help='Path to the PDF file to extract text from')
    parser.add_argument('output_file', type=str, help='Path to save the extracted text file')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Check if the input PDF file exists
    if not os.path.isfile(args.pdf_file):
        print(f"Error: The file '{args.pdf_file}' does not exist.")
        return
    
    # Try to extract text and handle any potential errors
    try:
        extract_text_from_pdf(args.pdf_file, args.output_file)
        print(f"Text extracted successfully to '{args.output_file}'")
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")

if __name__ == '__main__':
    main()

# TODO: Add support for batch processing of multiple PDF files
# TODO: Improve error handling for specific cases (e.g., corrupt PDFs, read/write permissions)
