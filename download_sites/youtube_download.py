from youtube_dl import YoutubeDL
from pprint import pprint
from time import time, sleep
import logging
import shutil
from os import listdir,remove
from os.path import isfile, join
import json

#FYI: to test quality options foy YT videos:  youtube-dl -F <link>

current_time = time()
## comment stuff, in case NO reading from JSON file is needed
# dir_name = ""  #
# format = "mp4" ## default is mp4  - do nothing
#                ## mp3 - convert to MP3
### set this to true, if the downloaded files on the SD card should be moved on the SSD drive
# move_to_ssd = True
# ssd_location = r"C:\DOWNLOADS\yt_cb_out\manual_dw\11"
# sd_card_location = join(r"E:\youtube", dir_name)
#data =  [
# [""]
# ]

## read from json
json_file = r"C:\Users\Andrei\Desktop\_youtube_dl_files.json"
with open(json_file, "r") as fh:
    json_data = json.load(fh)

# pprint (json_data)

## TODO
## counter will not work, if the element to download is a Youtube LIST
## it will register as 1 element
## the counting will not be appened to the file_name
## -> idea: see if the default numbering of youtube.dl for lists can be added to the filepath; IF-ELSE


output_dir = join(json_data["general_data"]["sd_card_dir"], json_data["general_data"]["sub_dir"])
format = json_data["general_data"]["format"]
data = json_data["links"]
move_to_ssd = json_data["general_data"]["move_to_ssd"]
numbered_videos = json_data["general_data"]["use_counter"]
transfer_dir = join(json_data["general_data"]["ssd_dir"], json_data["general_data"]["sub_dir"])
start_counter = int(json_data["general_data"]["start_counter"])
## links are separated by comma
data = data[0].split(",")

# ignore value from json file for the counter, if NO counting is needed
if numbered_videos != "True":
    start_counter = 0


total_nr_links = len(data)

# counter used in case we want to number the titles
counter = start_counter

ydl_opts = {
    'format': 'best',  # 'best', #'bestaudio/best',            # best - for video  bestaudio-for audio;
    'outtmpl': '{}\%(title)s.%(ext)s'.format(output_dir),
    # 'keep-video' : True,
    'keepvideo': True,
    # 'default-search' : 'ytsearch',
}

ydl_opt_mp3 ={
    "mp3":
        [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }]
        }
if format == "mp3":
    ydl_opts['postprocessors'] = ydl_opt_mp3["mp3"]
    ydl_opts['format'] = 'bestaudio/worst'

for element in data: # counter,element enumerate(data):
    if numbered_videos == "True":
        ydl_opts['outtmpl'] = r'{}\{}_%(title)s.%(ext)s'.format(output_dir, counter)
    ydl = YoutubeDL(ydl_opts)
    pprint(ydl_opts)

    print ("downloading {} out of {}".format((counter+1), total_nr_links))
    ## TODO - try catch if this error comes   
        #   raise HTTPError(req.full_url, code, msg, hdrs, fp)
        #   urllib.error.HTTPError: HTTP Error 403: Forbidden
    
    
    ydl.download([element])
    counter += 1


##if move_to_ssd = true - move the content downloaded on the SD card to the SSD drive
if move_to_ssd == "True":
    print ("\n\n MOVING TO SSD \n\n")
    onlyfiles = [f for f in listdir(output_dir) if isfile(join(output_dir, f))]
    for file in onlyfiles:
        if file.endswith(".mp4") or file.endswith(".mp3"):
            print ("moving {} to {}".format(file, join(transfer_dir,file)))
            shutil.move(join(output_dir, file), join(transfer_dir, file))
            sleep(2)
            print ("------move done-----")
    else:
        print ("\n\n NOT moving to SSD; file kept on SD-card \n\n")
    
current_time2 = time()
diff = current_time2 - current_time

pprint ("/n/n\t total time: \n {:.2f} seconds \n{:.2f} minutes\n {:.2f} hours".format(diff, (diff/60), (diff/3600)))
