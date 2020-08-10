import os
import PyPDF2

print(os.getcwd())

os.chdir("c:/users/gurpreet/desktop")
print(os.getcwd())


for i in os.listdir():
    if i == "REMUSE PDF.PDF" :

        print("File exists")  

        pdf_file = open("pdf.pdf", 'rb') 
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdf_file) 


        # creating a page object 
        page = pdfReader.getPage(0) 
        page1 = pdfReader.getPage(0) 

        
        # extracting text from page 
        print(page.extractText()) 
        pages = page1.extractText()

       
        data = pages.split(" ")
        print("## data ##",data)
        if "pdf995" in data:
            print(" #### yes")


        # closing the pdf file object 
        pdf_file.close() 
        

