import os
from PyPDF2 import PdfReader

# Directory containing your PDF files
directory_path = "./data/"

# Initialize variables to store the maximum length
max_length = 0
longest_paragraph = ""

# Loop through all PDF files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(directory_path, filename)

        # Load the PDF file
        reader = PdfReader(file_path)

        # Extract text from the PDF
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Split the text into paragraphs
        paragraphs = text.split("\n\n")

        # Find the length of each paragraph and track the maximum length
        for paragraph in paragraphs:
            if len(paragraph) > max_length:
                max_length = len(paragraph)
                longest_paragraph = paragraph

# Output the longest paragraph and its length
print(f"Max Paragraph Length: {max_length}")

