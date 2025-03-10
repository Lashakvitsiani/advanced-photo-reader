import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image, lang="eng+kat")
        print("\nExtracted Text:\n")
        print(extracted_text if extracted_text.strip() else "No text found in the image.")
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def upload_and_process():
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        extract_text(file_path)

root = tk.Tk()
root.withdraw() 

upload_and_process()
