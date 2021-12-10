
from youtube_dl import YoutubeDL
from pprint import pprint
from time import time, sleep

current_time = time()
#
#
#
# #"https://video.sekindo.com/uploads/cn2/video/users/hls/18709/video_5c45c136b3170453834695/vid5f3931a720b30343076847.mp4/w_480_00327.ts"
# # file_name_base = "https://video.sekindo.com/uploads/cn2/video/users/hls/18709/video_5c45c136b3170453834695/vid5f3931a720b30343076847.mp4/w_480_00"
# # file_name_ext = ".ts"
# #
# # data = []
# #
# #
# # for count in range(326):
# #     #    327.
# #     if count < 9:
# #         count= str("00" + str(count+1))
# #     elif count < 99:
# #         count= str("0" + str(count+1))
# #     else:
# #         count = str(count + 1)
# #
# #     temp = file_name_base + count + file_name_ext
# #
# #
# #     print(temp)
# #     # sleep(0.1)
# #
# #
# #     data.append(temp)
# data = []
#
# str1 = r"https://161vod-adaptive.akamaized.net/exp=1629731328~acl=%2F231451560%2F%2A~hmac=c22058b002337396d3ab44dff5840efd4f37706767e63b223538dc2ee8494cb7/231451560/sep/audio/820060884/chop/segment-{}.m4s"
# for x in range(1,301):
#     data.append(str1.format(x))
#
# ydl_opts = {
#             'format': 'best', #'bestaudio/best',            # best - for video  bestaudio-for audio;
#             'outtmpl': 'D:/DOWNLOADS/yt_cb_out/radiology1/%(title)s.%(ext)s',
#             'keep-video' : True,
#             }
#
# ydl = YoutubeDL(ydl_opts)
# ydl.download(data)
#
# current_time2 = time()
# diff = current_time2 - current_time
#
# pprint ("--------------------total time: {} seconds - {} minutes ---------------".format(diff, (diff/60)))
#



from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_merge_video_audio, ffmpeg_resize,ffmpeg_movie_from_frames

ffmpeg_movie_from_frames(r"D:\DOWNLOADS\yt_cb_out\radiology1\abc.mp4", r"D:\DOWNLOADS\yt_cb_out\radiology1", 30)


