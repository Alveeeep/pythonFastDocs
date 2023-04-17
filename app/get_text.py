from docx2python import docx2python

# extract docx content
doc_result = docx2python('okpd.docx')
for el in doc_result.body[25:60]:
    for i in el:
        print(i)
