import os.path

from mutagen.easyid3 import EasyID3
from os import walk, path
audio = EasyID3("default.mp3_c1c2b63d27d16c5392e9bcee5ba2de76_36148938.mp3")
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
forbidden_chars_win = [ "<", ">", ":", " ", "/",   "\\",  "|", "?", "*",]
mydir = r"E:\x"
myfiles = []
for root, dirs, files in walk(mydir, topdown=False):
    myfiles =files

for file in myfiles:
    file = os.path.join(mydir, file)
    pprint ( file)
    audio = EasyID3(file)
    # print (audio['title'])
    new_name =os.path.join(mydir,audio['title'][0])

    new_name = new_name + ".mp3"


    print (new_name)
    os.rename(file, new_name)



# from mutagen.mp3 import MP3
# audio = MP3("default.mp3_c1c2b63d27d16c5392e9bcee5ba2de76_36148938.mp3")
# print (audio.info.  pprint ((audio.info.length))
#
