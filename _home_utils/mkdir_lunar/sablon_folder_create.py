## based on a config file, create a folder structure for each apartment,
## with needed bills, exceptions, email to send to, notifistions etc
## created it each month
## TODO - finda  way to store the results, long(ish) term

## TODO - add a total.txt file

# TODO  - remuve duplicated code!!!!!
## all FOR loops, like line 43-> 85

import os 
from pprint import pprint    
from datetime import datetime


#path = os.path.join(parent_dir, directory) 
#os.mkdir(path) 
# print("Directory '%s' created" %directory) 
   
parent_dir = r"E:\WORK\fact_struct2"

def create_subdir_name(ap_name):
    subir_name = ""
    
    current_month = str( int( datetime.now().strftime('%m') )- 1 )
    
    current_year = datetime.now().strftime('%Y') 
   
    subir_name = current_year + "_" + current_month  + "_" + ap_name
       
    return subir_name

if os.path.exists(parent_dir):
    pass
else:
    pprint ("creating %s"  %parent_dir) 
    os.mkdir(parent_dir) 


c24 = {
    "facturi":["gaz", "curent", "intretinere"],
    "email": "vianney",
    "observatii": ["3,6,9,12: trimis rent receipt", "fisier cu total"]
}

for key in c24.keys():
    print (key)
    
    full_name = create_subdir_name("c24")
    full_name = os.path.join(parent_dir,full_name)
    
    ## create folder for current month
    if os.path.exists(full_name):
        pass
    else:
        pprint ("/n")
        pprint ("creating %s"  %full_name) 
        os.mkdir(full_name) 
    
    print (full_name)

    ## creeate file with email
    if key == "email":
        filename = "_" + key+".txt"
        pprint (os.path.join(full_name,filename))
                            
        with open (  os.path.join(full_name,filename), 'w+') as my_file:
            my_file.write(c24[key])
    
    # create files for each factura             
    if key == "facturi":
        for el in c24[key]:
            el = el+".txt"
            pprint (os.path.join(full_name,el))
                               
            with open (  os.path.join(full_name,el), 'w+') as my_file:
                my_file.write("_")

    # observatii
    if key == "observatii":
        filename = "_" + key+".txt"
        for el in c24[key]:
            with open (  os.path.join(full_name, filename), 'a+') as my_file:
                my_file.write(el)
                my_file.write("\n")
                
    ## TODO: sa nu se suprascrie fisiere si foldere
    ## IF  EXISTS - DONT    

#############################
c35 = {
    "facturi":["gaz", "curent"],
    "email": "ionut",
    "observatii": ["scazut 20 Ron fond rulemtn"]    
}

for key in c35.keys():
    print (key)
    
    full_name = create_subdir_name("c35")
    full_name = os.path.join(parent_dir,full_name)
    
    ## create folder for current month
    if os.path.exists(full_name):
        pass
    else:
        pprint ("/n")
        pprint ("creating %s"  %full_name) 
        os.mkdir(full_name) 
    
    print (full_name)

    ## creeate file with email
    if key == "email":
        filename = "_" + key+".txt"
        pprint (os.path.join(full_name,filename))
                            
        with open (  os.path.join(full_name,filename), 'w+') as my_file:
            my_file.write(c35[key])
    
    # create files for each factura             
    if key == "facturi":
        for el in c35[key]:
            el = el+".txt"
            pprint (os.path.join(full_name,el))
                               
            with open (  os.path.join(full_name,el), 'w+') as my_file:
                my_file.write("_")

    # observatii
    if key == "observatii":
        filename = "_" + key+".txt"
        for el in c35[key]:
            with open (  os.path.join(full_name, filename), 'a+') as my_file:
                my_file.write(el)
                my_file.write("\n")
                
    ## TODO: sa nu se suprascrie fisiere si foldere
    ## IF  EXISTS - DONT    
#############################
k34 = {
    "facturi":["intretinere", "curent", "rds"],
    "email": "maho",
    "exceptii": "nu",
    "observatii": ["verificat scazut 20 Ron fond rulemtn"],    
 }

for key in k34.keys():
    print (key)
    
    full_name = create_subdir_name("k34")
    full_name = os.path.join(parent_dir,full_name)
    
    ## create folder for current month
    if os.path.exists(full_name):
        pass
    else:
        pprint ("/n")
        pprint ("creating %s"  %full_name) 
        os.mkdir(full_name) 
    
    print (full_name)

    ## creeate file with email
    if key == "email":
        filename = "_" + key+".txt"
        pprint (os.path.join(full_name,filename))
                            
        with open (  os.path.join(full_name,filename), 'w+') as my_file:
            my_file.write(k34[key])
    
    # create files for each factura             
    if key == "facturi":
        for el in k34[key]:
            el = el+".txt"
            pprint (os.path.join(full_name,el))
                               
            with open (  os.path.join(full_name,el), 'w+') as my_file:
                my_file.write("_")

    # observatii
    if key == "observatii":
        filename = "_" + key+".txt"
        for el in k34[key]:
            with open (  os.path.join(full_name, filename), 'a+') as my_file:
                my_file.write(el)
                my_file.write("\n")
    
    # ## fisier pt total
    # default_total = "total"        
    # filenametotal = default_total+".txt"        
    # with open (  os.path.join(full_name, filename), 'a+') as my_file:
    
    ## TODO: sa nu se suprascrie fisiere si foldere
    ## IF  EXISTS - DONT    

#############################
ap38 = {
    "facturi":["gaz", "curent", "intretinere", "parcare"],
    "email": "poza",
    "observatii": ["scazut 50 Ron fond rulemtn", "Facut poza"],    
 }

for key in ap38.keys():
    print (key)
    
    full_name = create_subdir_name("ap38")
    full_name = os.path.join(parent_dir,full_name)
    
    ## create folder for current month
    if os.path.exists(full_name):
        pass
    else:
        pprint ("/n")
        pprint ("creating %s"  %full_name) 
        os.mkdir(full_name) 
    
    print (full_name)

    ## creeate file with email
    if key == "email":
        filename = "_" + key+".txt"
        pprint (os.path.join(full_name,filename))
                            
        with open (  os.path.join(full_name,filename), 'w+') as my_file:
            my_file.write(ap38[key])
    
    # create files for each factura             
    if key == "facturi":
        for el in ap38[key]:
            el = el+".txt"
            pprint (os.path.join(full_name,el))
                               
            with open (  os.path.join(full_name,el), 'w+') as my_file:
                my_file.write("_")

    # observatii
    if key == "observatii":
        filename = "_" + key+".txt"
        for el in ap38[key]:
            with open (  os.path.join(full_name, filename), 'a+') as my_file:
                my_file.write(el)
                my_file.write("\n")
                
    ## TODO: sa nu se suprascrie fisiere si foldere
    ## IF  EXISTS - DONT    

# dir_struct = {}

# apart_dic = {
#     "name": 
#     # full name = name + year + month + name
#     lista_facturi = []
#     lista_obsetrvatiii = []
    
#     "email":
# ]}


# "c24" = {
#     "facturi":["gaz", "curent", "intretinere"],
#     "email": "vianney",
#    
#     "observatii": [" 3,6,9,12: trimsi rent receipt", "fisier cu total"]
# }

# "c35" = {
#     "facturi":["gaz", "curent"],
#     "email": "ionut",
#     "observatii": []"scazut 20 Ron fond rulemtn"]    
# }

# "k34" = {
#     "facturi":["gaz", "curent", "rds"],
#     "email": "maho",
#     "exceptii": 
#     "observatii": ["verificat scazut 20 Ron fond rulemtn",],    
#  }

# "38" = {
#     "facturi":["gaz", "curent", "intretinere", "parcare"],
#     "email": "poza",
#     "observatii": ["scazut 50 Ron fond rulemtn", "Facut poza"],    
#  }
# #"ap4"
# #"ap8"
# # J29