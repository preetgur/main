import os
import PyPDF2

print(os.getcwd())

os.chdir("c:/users/gurpreet/desktop")
print(os.getcwd())


for i in os.listdir():
    if i == "REMUSE PDF.PDF" :

        print("File exists")  

        pdf_file = open("pnb.pdf", 'rb') 
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdf_file) 

        # printing number of pages in pdf file 
        # print(pdfReader.numPages) 
        # print(pdfReader.getDocumentInfo())
        # print(pdfReader.getDocumentInfo().subject)
        # print(pdfReader.getDocumentInfo().title)

        if pdfReader.isEncrypted:
        
            pdfReader.decrypt('APK010281')
            # printing number of pages in pdf file 
            print(pdfReader.numPages) 
            print(pdfReader.getDocumentInfo())
            print(pdfReader.getDocumentInfo().subject)
            print(pdfReader.getDocumentInfo().title)

        # creating a page object 
        page = pdfReader.getPage(0) 
        # page1 = pdfReader.getPage(1) 

        
        # extracting text from page 
        print(page.extractText()) 
        # pages = page1.extractText()
        # print(page1.extractText()) 
        # print(type(pages))

        # if "Pdf955" in pages:
        #     print("yes")


        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(pdfReader.getPage(1)) # copy data from page 1 from above file
        pdfWriter.encrypt('swordfish')  

        resultPdf = open('encryptedminutes.pdf', 'wb') # create new file
        pdfWriter.write(resultPdf)
        resultPdf.close()
        # closing the pdf file object 
        pdf_file.close() 
        

