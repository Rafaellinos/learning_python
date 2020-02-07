import sys

try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError as err:
    print("please install PyPDF2: pip3 install PyPDF2")
    exit()


def watermark(input_pdf, watermark_pdf):
    if not input_pdf.endswith('.pdf') or not watermark_pdf.endswith('.pdf'):
        print("Those files must be pdfs")
        exit()

    pdf = PdfFileReader(open(input_pdf, 'rb'))
    water_mark = PdfFileReader(open(watermark_pdf, 'rb'))
    output = PdfFileWriter()

    for i in range(pdf.getNumPages()):
        p = pdf.getPage(i)
        p.mergePage(water_mark.getPage(0))
        output.addPage(p)

    with open('watermarked.pdf', 'wb') as new_file:
        output.write(new_file)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough arguments, must have 1 file the is the watermark and another on to be marked.")
        exit()

    watermark(sys.argv[1], sys.argv[2])

