## based on a config file, create a folder structure for each apartment,
## with needed bills, exceptions, email to send to, notifistions etc
## created it each month
## TODO - finda  way to store the results, long(ish) term

## TODO - add a total.txt file

import os 
from pprint import pprint    
from datetime import datetime


#path = os.path.join(parent_dir, directory) 
#os.mkdir(path) 
# print("Directory '%s' created" %directory) 
   
parent_dir = r"E:\WORK\fact_struct2"

pprint ("=========== current dir  %s =========="  %parent_dir) 


def create_subdir_name(ap_name):
    subdir_name = ""
    
    current_month = str( int( datetime.now().strftime('%m') )- 1 )
    current_year = datetime.now().strftime('%Y') 
   
    subdir_name = current_year + "_" + current_month  + "_" + ap_name
       
    return subdir_name

##############################################################################
##############################################################################
##############################################################################

# create top level dir
if os.path.exists(parent_dir):
    pass
else:
    pprint ("creating %s"  %parent_dir) 
    os.mkdir(parent_dir) 


## dict with all apartments with each specific info
# for each apt - give 'facturi', 'email' and 'observatii'
apart_list = {
    "c24" : {
        "facturi":["gaz", "curent", "intretinere"],
        "fond_rul":"0",
        "email": "vianney",
        "observatii": ["3,6,9,12: trimis rent receipt"]
    },

    "c35": {
        "facturi":["gaz", "curent"],
        "email": "ionut",
        "fond_rul":"-20",
        "observatii": ["scazut 20 Ron fond rulemtn"]    
    },

    "k34": {
        "facturi":["intretinere", "curent", "rds"],
        "email": "maho",
        "fond_rul":"-20",
        "observatii": ["scazut 20 Ron fond rulemtn"],    
    },

    "ap38" : {
        "facturi":["gaz", "curent", "intretinere", "parcare"],
        "email": "poza",
        "fond_rul":"-50",
        "observatii": ["scazut 50 Ron fond rulemtn", "Facut poza"],    
    }

# #"ap4"
# #"ap8"
# # J29
}

for apart in apart_list.keys():
    full_name = create_subdir_name(str(apart))
    full_name = os.path.join(parent_dir,full_name)
    
    ## create folder for current month for each apt 
    if os.path.exists(full_name):
        pass
    else:
        pprint ("/n")
        pprint ("creating %s"  %full_name) 
        os.mkdir(full_name) 
    print (full_name)
 
    # handle each apt    
    for key in apart_list[apart].keys():

        ## creeate file with email / contact info
        if key == "email":
            filename = "_" + key+".txt"
            pprint (os.path.join(full_name,filename))
                                
            with open (  os.path.join(full_name,filename), 'w+') as my_file:
                my_file.write(apart_list[apart][key])
        
        # create files for each factura             
        if key == "facturi":
            for el in apart_list[apart][key]:
                el = el+".txt"
                pprint (os.path.join(full_name,el))
                                
                with open (  os.path.join(full_name,el), 'w+') as my_file:
                    my_file.write("_")

        # observatii - put info in a file
        if key == "observatii":
            filename = "_" + key+".txt"
            for el in apart_list[apart][key]:
                with open (  os.path.join(full_name, filename), 'a+') as my_file:
                    my_file.write(el)
                    my_file.write("\n")

        # total - create total.txt with each value
        filename_t = "total.txt"
        if os.path.exists(  os.path.join(full_name, filename_t) ):
            pass 
        else:
            with open (  os.path.join(full_name, filename_t), 'a+') as my_file:
                for el in apart_list[apart]["facturi"]:        
                    my_file.write(el)
                    #my_file.write("\t"*int((12-len(el))/4)) 
                    my_file.write("\n")
                if int (apart_list[apart]["fond_rul"]) != 0:
                    my_file.write( "fond_rul \t %s" % apart_list[apart]["fond_rul"])
                    my_file.write("\n")
                my_file.write("total")
            
        ## TODO: sa nu se suprascrie fisiere si foldere
        ## IF  EXISTS - DONT    

