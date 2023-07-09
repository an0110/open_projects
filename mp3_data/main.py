import os.path

from mutagen.easyid3 import EasyID3
from os import walk, path
#audio = EasyID3("TLFIE1099471131.mp3")
# audio['title'] = u"Example Title"
# audio['artist'] = u"Me"
# audio['album'] = u"My album"
# audio['composer'] = u"" # clear
# audio.save()
from pprint import pprint


# pprint (dir (audio))
# for key in audio.keys():
#     print("{} - {}".format(key, audio[key]))
# print (audio)
# os.rename(old, new)
forbidden_chars_win = [ "<", ">", ":",  "/",   "\\",  "|", "?", "*",] #" ",
mydir = r"C:\DOWNLOADS\yt_cb_out\manual_dw\_AUDIO\siemens_av_podcat"
myfiles = []
for root, dirs, files in walk(mydir, topdown=False):
    myfiles =files

for file in myfiles:
    file = os.path.join(mydir, file)
    pprint ( file)
    audio = EasyID3(file)
    new_name = audio['title'][0]
    for f in forbidden_chars_win:
        new_name = new_name.replace(f, " ")
    new_name =os.path.join(mydir,new_name)
    #exit()
    new_name = new_name + ".mp3"

    print (new_name)
    os.rename(file, new_name)
