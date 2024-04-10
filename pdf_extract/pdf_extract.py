from pypdf import PdfReader
from pathlib import Path
from pprint import pprint 


def read_ENEL():
    
    pdf_path = r"E:\WORK\PDF_extract\Factura_ENEL_nr-24EI04757389_10.03.2024.pdf" 

    pdf_reader = PdfReader(pdf_path)

    print ("number of files:" + str(len(pdf_reader.pages)) )

    page1_object = pdf_reader.pages[0]

    # pprint (dir (page1_object))

    textPage1 = page1_object.extract_text()

    # //pprint ()
    # with open(r"C:\WORK\repos\open_projects\pdf_extract\out.txt", 'w',encoding='UTF-8') as f:
    #     print(textPage1,  file=f)  # Python 3.x

    # 6.  Total de plată (6=4+5)



    textPage1_array = textPage1.splitlines()

    print (textPage1_array[40])

    for line in textPage1_array:
        if line.startswith("6.  Total de plată (6=4+5)"):
            print (line)
            exit()


def read_cheltuieli():
    
    pdf_path = r"E:\WORK\PDF_extract\tabel luna ianuarie 2024 Iris 6 - fara nume proprietari.pdf" 

    pdf_reader = PdfReader(pdf_path)

    print ("number of files:" + str(len(pdf_reader.pages)) )

    page1_object = pdf_reader.pages[0]
    page2_object = pdf_reader.pages[1]

    # pprint (dir (page1_object))

    # textPage1 = page1_object.extract_text()
    textPage2 = page2_object.extract_text()

    # pprint ()
    with open(r"C:\WORK\repos\open_projects\pdf_extract\out.txt", 'w',encoding='UTF-8') as f:
        # print(textPage1,  file=f)  # Python 3.x
        print(textPage2,  file=f)  # Python 3.x

    # 6.  Total de plată (6=4+5)


    # exit()
    textPage2_array = textPage2.splitlines()

    # print (textPage2_array[40])



    for line in textPage2_array:
        if line.startswith("38"):
            line_arr = line.split(" ")
            if line_arr[-1] == "38":
                print (line)
                print ("\ncheltuieli pt AP 38:\n" + line_arr[-2])
                exit()
            
            
read_cheltuieli()