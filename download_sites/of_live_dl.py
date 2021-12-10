


from youtube_dl import YoutubeDL
from pprint import pprint
from time import time, sleep











stream_path = r"https://stream1-dc2.onlyfans.com/hls/dc2-room-7UY8xGjBshQLY/2/index437.ts"


for second in range(860, 9999999, 1):


    stream_path_tmpl =[r"https://stream1-dc2.onlyfans.com/hls/dc2-room-7UY8xGjBshQLY/2/index{}.ts".format(second)]
    print (stream_path_tmpl)
    # exit()

    ydl_opts = {

                'format': 'best', #'bestaudio/best',            # best - for video  bestaudio-for audio;
                'outtmpl': 'D:/DOWNLOADS/yt_cb_out/radiology1/%(title)s.%(ext)s',
                'keep-video' : True,
                }

    ydl = YoutubeDL(ydl_opts)
    ydl.download(stream_path_tmpl)
    sleep(1)