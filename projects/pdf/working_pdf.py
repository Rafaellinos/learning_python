"""
pip3 install PyPDF2
"""
import PyPDF2

"""
modes:
rb = read binary
wb = write binary
"""
with open("ata1.pdf", 'rb') as file:

    reader = PyPDF2.PdfFileReader(file) # only can read if is binary obj
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90) # rotate pdf
    writer = PyPDF2.PdfFileWriter() # instanciate the writer
    writer.addPage(page) # give the page rotated to writer
    with open('new.pdf', 'wb') as new_file:
        writer.write(new_file) # open a new file as binary as save with the writer
