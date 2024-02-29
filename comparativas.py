import os
import shutil
import PyPDF2
import difflib
import re

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def compare_pdfs(pdf_file1, pdf_file2):
    # Function to compare the text content of two PDFs
    with open(pdf_file1, 'rb') as file1:
        pdf_text1 = ' '.join([page.extract_text() for page in PyPDF2.PdfReader(file1).pages])

    with open(pdf_file2, 'rb') as file2:
        pdf_text2 = ' '.join([page.extract_text() for page in PyPDF2.PdfReader(file2).pages])

    return difflib.SequenceMatcher(None, pdf_text1, pdf_text2).ratio()

def categorize_pdfs(input_folder, output_folder, threshold=0.5):
    # Function to categorize PDFs based on structural similarity
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        dest_folder = None

        for category_folder in os.listdir(output_folder):
            category_path = os.path.join(output_folder, category_folder)

            for existing_file in os.listdir(category_path):
                existing_file_path = os.path.join(category_path, existing_file)

                similarity = compare_pdfs(pdf_path, existing_file_path)
                if similarity >= threshold:
                    dest_folder = category_path
                    break

            if dest_folder:
                break

        if not dest_folder:
            #category_name = f"Category_{len(os.listdir(output_folder)) + 1}"
            category_name = f"Tipo_{len(os.listdir(output_folder)) + 1}"
            dest_folder = os.path.join(output_folder, sanitize_filename(category_name))
            os.makedirs(dest_folder)

        shutil.copy(pdf_path, dest_folder)

if __name__ == "__main__":
    input_folder = "C:\\Users\\atrasfi\OneDrive - Uber Freight\Documents\Files"   # Replace with the path to the folder containing PDFs
    output_folder = "C:\\Users\\atrasfi\OneDrive - Uber Freight\Documents\Files\dif"  # Replace with the path to the folder for categorized PDFs
    threshold = 0.5  # Adjust the threshold as needed for similarity comparison

    categorize_pdfs(input_folder, output_folder, threshold)
