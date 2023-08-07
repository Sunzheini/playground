from PyPDF2 import PdfReader


# file_pathz = 'C:\\Users\\User\\Desktop\\demo19.pdf'
# file_pathz = 'C:\\Users\\User\\Desktop\\Scherz.pdf'
file_pathz = r'C:/Users/User/Desktop/P1/mark-21_268-viking-vert_plan_sklad_new_06_02_2019-v2(2).pdf'


# def extract_text_from_pdf(file_path):
#     with open(file_path, 'rb') as f:
#         pdf = PdfReader(f)
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text


# def extract_text_from_pdf(file_path):
#     with open(file_path, 'rb') as f:
#         pdf = PdfReader(f)
#         text = pdf.pages[4].extract_text()
#     return text

# def extract_text_from_pdf(file_path):
#     doc = fitz.open(file_path)
#     page = doc[3]
#     text = page.get_text("text")
#     return text


import cv2
import numpy as np
import fitz  # PyMuPDF
import pytesseract
from PIL import Image, ImageEnhance

# def extract_text_from_pdf(file_path):
#     doc = fitz.open(file_path)
#     page = doc[6]  # get the first page
#     pix = page.get_pixmap()
#     mode = "RGBA" if pix.alpha else "RGB"
#     img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
#     text = pytesseract.image_to_string(img)
#     return text


# def extract_text_from_pdf(file_path):
#     doc = fitz.open(file_path)
#     page = doc[1]  # get the first page
#
#     # Define the rectangle that contains the text you're interested in.
#     # The coordinates are in PDF points (72 points = 1 inch), and the origin is the top-left corner of the page.
#     # You'll need to adjust these values based on where the text is located in your PDFs.
#     # rect = fitz.Rect(50, 50, 200, 200)  # x1, y1, x2, y2
#     rect = fitz.Rect(100, 75, 130, 95)  # x1, y1, x2, y2
#
#     # Get a pixmap of the specific area of the page.
#     pix = page.get_pixmap(clip=rect)
#
#     mode = "RGBA" if pix.alpha else "RGB"
#     img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
#
#     # Display the image.
#     img.show()
#
#     text = pytesseract.image_to_string(img)
#     return text


def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    page = doc[0]  # get the first page

    # Define the rectangle that contains the text you're interested in.
    # rect = fitz.Rect(100, 75, 130, 95)  # x1, y1, x2, y2
    rect = fitz.Rect(550, 450, 650, 550)  # x1, y1, x2, y2

    # Get a pixmap of the specific area of the page.
    pix = page.get_pixmap(clip=rect)

    mode = "RGBA" if pix.alpha else "RGB"
    img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)

    # Resize image
    img = img.resize((img.width*2, img.height*2), Image.BICUBIC)

    # Increase contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)

    # Convert image to grayscale and apply Gaussian blur and adaptive threshold using OpenCV
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    img_cv = cv2.GaussianBlur(img_cv, (5, 5), 0)
    img_cv = cv2.adaptiveThreshold(img_cv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Convert back to PIL Image
    img = Image.fromarray(img_cv)

    # Display the image.
    img.show()

    # Specify Tesseract configuration options
    config = '--oem 3 --psm 6'

    text = pytesseract.image_to_string(img, config=config)
    return text


text = extract_text_from_pdf(file_pathz)
print(text)
