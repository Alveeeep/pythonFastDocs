from docx2python import docx2python
from PyPDF2 import PdfReader

pdf_document = "616.pdf"
with open(pdf_document, "rb") as filehandle:
   pdf = PdfReader(filehandle)
   page1 = pdf.pages[17]
   print(page1.get_contents())
   print(page1.extract_text())
# extract docx content
# doc_result = docx2python('C:/Users/amisalimov/PycharmProjects/pythonFastDocs/app/ogranicheniya471.docx')
# for el in doc_result.body:
#    for i in el:
#        print(i)


