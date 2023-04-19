from docx2python import docx2python

# extract docx content
doc_result = docx2python('C:/Users/amisalimov/PycharmProjects/pythonFastDocs/app/ogranicheniya471.docx')
for el in doc_result.body:
    for i in el:
        print(i)
