from youtube_dl import YoutubeDL
from pprint import pprint
from time import time, sleep
import logging
import threading
import shutil
from os import listdir,remove
from os.path import isfile, join
import json

current_time = time()

## TODO:
# ## create a batch file to put all links from youtube to download, without opening pycharm
# 1. create file with each link on a line
# 2     call this .py to read and download
# 3 open manul_doanloads folder when finished

dir_name = "11/threads4"  #
format = "mp4" ## default is mp4  - do nothing
               ## mp3 - convert to MP3
## put this to true, for a pause between each file - will help ?
sleep_between_dwl = False
### set this to true, if the downloaded files on the SD card should be moved on the SSD drive
move_to_ssd = True


## TODO read from json
# json_file = r""
# with open(json_file, "r") as fh:
#     json_data = json.load(fh)
#
# dir_name = json_data["dir_name"]
# format = json_data["format"]
# data = json_data["data"]




exit()



data =  [
["https://www.youtube.com/watch?v=9p_QW_HsKPI"],
["https://www.youtube.com/watch?v=XW-Eb6i9i5I"],

]
counter = 1

ydl_opt_mp3 ={ "mp3":
                    [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                    }]
                }
#to test quality options:  youtube-dl -F <link>

ydl_opts = {
    'format': 'best',  # 'best', #'bestaudio/best',            # best - for video  bestaudio-for audio;
    # 'outtmpl': 'D:/DOWNLOADS/yt_cb_out/manual_dw/huberman_audio/{}_%(title)s.%(ext)s'.format(counter),
    # 'outtmpl': 'D:/DOWNLOADS/yt_cb_out/manual_dw/{}/{}_%(title)s.%(ext)s'.format(dir_name, counter),
    'outtmpl': 'E:\youtube\{}\%(title)s.%(ext)s'.format(dir_name),
    # 'keep-video' : True,
    'keepvideo': True,
    # 'default-search' : 'ytsearch',
}

if format == "mp3":
    ydl_opts['postprocessors'] = ydl_opt_mp3["mp3"]

pprint(ydl_opts)
ydl = YoutubeDL(ydl_opts)

thread_dict = {}




for element in data:
    thread_dict[element[0]] =  (threading.Thread (target=ydl.download, args=(element,)))

for k, v in thread_dict.items():
    print ("{} started downloading ".format(k))
    k = v
    k.start()
    k.join()

#     if sleep_between_dwl:
#         print ("... sleeping 5 seconds ...")
#         sleep(10)
#
#
# # if move_to_ssd = true - move the content downloaded on the SD card to the SSD drive
# ssd_location = r"C:\DOWNLOADS\yt_cb_out\manual_dw\11"
# to_inspect = r"E:\youtube\11"
# if move_to_ssd:
#     onlyfiles = [f for f in listdir(to_inspect) if isfile(join(to_inspect, f))]
#     for file in onlyfiles:
#         if file.endswith(".mp4"):
#
#             logging.info ("moving {} to {}".format(file, join(ssd_location,file)))
#             shutil.move(join(to_inspect, file), join(ssd_location, file))
#             sleep(2)
#             logging.info ("------move done-----")
#
current_time2 = time()
diff = current_time2 - current_time

pprint ("\n\n\t total time: \n {:.2f} seconds \n{:.2f} minutes\n {:.2f} hours".format(diff, (diff/60), (diff/3600)))
