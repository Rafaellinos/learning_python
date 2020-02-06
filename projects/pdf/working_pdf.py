"""
pip3 install PyPDF2
"""
import PyPDF2

"""
modes:
rb = read binary
"""
with open("ata1.pdf", 'rb') as file:

    reader = PyPDF2.PdfFileReader(file) # only can read if is binary obj
    print(reader.numPages)
    page = reader.getPage(0)
