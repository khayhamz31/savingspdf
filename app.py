import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from PIL import Image, ImageTk

from processor.pdf_processor import extract_text_from_pdf
from processor.parser import parse_transactions
from utils.helpers import ensure_folder, safe_filename

PDF_FOLDER = "pdfs"
ensure_folder(PDF_FOLDER)

def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    # Save PDF
    filename = safe_filename(os.path.basename(file_path))
    save_path = os.path.join(PDF_FOLDER, filename)
    shutil.copy(file_path, save_path)
    messagebox.showinfo("Saved", f"PDF saved to {save_path}")

    # Display first page
    import fitz
    doc = fitz.open(save_path)
    page = doc[0]
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.thumbnail((400, 500))
    img_tk = ImageTk.PhotoImage(img)
    pdf_label.config(image=img_tk)
    pdf_label.image = img_tk

    # Extract text
    text = extract_text_from_pdf(save_path)
    print("Text preview:\n", text[:500])  # first 500 chars

    # Parse transactions
    df = parse_transactions(text)
    print("\nParsed transactions:\n", df.head())

# GUI
root = tk.Tk()
root.title("Bank Statement Analyzer")
root.geometry("500x600")

upload_btn = tk.Button(root, text="Upload Bank Statement PDF", command=upload_pdf, height=2, width=30)
upload_btn.pack(pady=10)

pdf_label = tk.Label(root)
pdf_label.pack(pady=10)

root.mainloop()