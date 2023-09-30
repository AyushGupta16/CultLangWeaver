
import os
from io import StringIO
from pdfminer.high_level import extract_text
from PIL import Image
import pytesseract
import cv2
import numpy as np
def upload_file():
    # Get the file from the user.
    file = request.files['file']
    # Save the file to a temporary location.
    filename = os.path.join(os.getcwd(), 'uploads', file.filename)
    file.save(filename)
    return filename
def extract_text(filename):
    # Check if the file is a PDF or an image.
    if filename.endswith('.pdf'):
        # Extract text from the PDF file.
        text = extract_text(filename)
    elif filename.endswith('.jpg') or filename.endswith('.png'):
        # Extract text from the image file.
        image = Image.open(filename)
        text = pytesseract.image_to_string(image)
    else:
        # The file is not a PDF or an image.
        return None
    # Return the extracted text.
    return text
def main():
    # Upload the file.
    filename = upload_file()
    # Extract text from the file.
    text = extract_text(filename)
    # Print the extracted text.
    print(text)
if __name__ == '__main__':
    main()
