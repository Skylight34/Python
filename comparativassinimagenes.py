import os
import shutil
import PyPDF2
import re
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
import pytesseract

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def remove_text_and_codes(pdf_file, output_folder):
    # Function to remove text, barcodes, and QR codes from a PDF and save the skeleton images
    images = convert_from_path(pdf_file)

    for i, image in enumerate(images):
        image = remove_codes_from_image(image)
        image.save(os.path.join(output_folder, f"Page_{i+1}.png"), "PNG")

def remove_codes_from_image(image):
    # Function to remove QR codes and barcodes from the image
    decoded_objects = decode(image)
    for obj in decoded_objects:
        if obj.type == 'QRCODE' or obj.type == 'CODE128':
            image = image.crop(obj.rect)
    return image

if __name__ == "__main__":
    input_folder = "C:\\Users\\atrasfi\OneDrive - Uber Freight\Documents\Files"   # Reemplaza con la ruta a la carpeta que contiene los reportes PDF
    output_folder = "C:\\Users\\atrasfi\OneDrive - Uber Freight\Documents\Files\dif"  # Reemplaza con la ruta a la carpeta para las imágenes de esqueletos

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    pytesseract.pytesseract.tesseract_cmd = r'ruta_de_tesseract_executable'  # Reemplaza con la ruta al ejecutable de Tesseract OCR

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        remove_text_and_codes(pdf_path, output_folder)

