import sys
import os

try:
    from PyPDF2 import PdfFileMerger
except ImportError as err:
    print("please install PyPDF2: pip3 install PyPDF2")
    exit()

def merge_pdf(pdf_list):
    merger = PdfFileMerger()
    try:
        for pdf in pdf_list:
            if pdf.endswith(".pdf"): merger.append(pdf)
        merger.write('merged.pdf')
    except Exception as err:
        print(f"Erro: {err}")


if len(sys.argv) < 3:
    print("Not enough arguments, must have at least 2 pdfs to merge.")
    exit()

merge_pdf(sys.argv[1:])

