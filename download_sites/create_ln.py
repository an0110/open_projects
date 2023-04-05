
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




# str1 = r"https://hls2.videos.sproutvideo.com/8fd886640bdf591152527f12d959e174/b2809eab67c9c487cdbd734b68a6a811/video/1080_00001.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9obHMyLnZpZGVvcy5zcHJvdXR2aWRlby5jb20vOGZkODg2NjQwYmRmNTkxMTUyNTI3ZjEyZDk1OWUxNzQvYjI4MDllYWI2N2M5YzQ4N2NkYmQ3MzRiNjhhNmE4MTEvKi50cz9zZXNzaW9uSUQ9YzlhZDA0ODItMjk5My00ZjA3LWJhY2YtMGQ4YzNhMjFkYWRjIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjM5ODM3MjA4fX19XX0_&Signature=IkSpxPO1KcN5ENRooAhzuGyUwqS4jLwPu~KXFSvpcOEUaNdx0knatzmIhlMcMM-pNHjbO~N3stnmBUBttOpazQJM9OUPlXHv8JhTxlzaGq4eLV8~S0UVa-CIT~T3XXNDGphA2~XJjNieRKX9GBSIJGVqNqNS3M5Nm2OsHkE025pHzCL08tILoB~C6nWRfzJDFX1UBnO1kD64WPHOygJEiTlmOLIl1I4cf64bE9ppMO9iutyU2pqacpW3GkPetJBrY2K99yq8mVJd2K8hO2w1HaSU~USx~GKcZmPFdT35eL9gWXTZG5zfr-NTCntUqFpjyFe23bpCasuyPdW4N1XEVA__&Key-Pair-Id=APKAIB5DGCGAQJ4GGIUQ&sessionID=c9ad0482-2993-4f07-bacf-0d8c3a21dadc"
# # for x in range(1,301):
# #     data.append(str1.format(x))
# data = [str1]




### STEP 1^- download the parts
data = []
# https://dood.so/e/oaernwz4wz119m2ty1e4pzporf28pbw
strx = r"https://www.bbc.co.uk/sounds/play/m0011s25"
# strx = r"https://s16.upstreamcdn.co/hls/w47rzdmfnfbnx2nroyqkgvnoiy33hbmrivlymcyuedtf5iv6lz24rdgq56uq/seg-{}-v1-a1.ts"
strx = r"https://psv150-1.crazycloud.ru/videos/-187217911/456242962/720.mp4/seg-{}-v1-a1.ts?extra=v1loNG_isxIr6zE2S-jY0Q&extra_info=bxKGAqpU8gytWHDiQNIWGvHF"

for c in range(108,305):
    data.append(strx.format(c))

ydl_opts = {
            'format': 'best', #'bestaudio/best',            # best - for video  bestaudio-for audio;
            'outtmpl': 'E:\save\%(title)s.%(ext)s',
            'keep-video' : True,
            }

ydl = YoutubeDL(ydl_opts)
ydl.download(data)

### step 2 - merge them
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_merge_video_audio, ffmpeg_resize,ffmpeg_movie_from_frames
#
# ffmpeg_movie_from_frames(r"E:\youtube\x\full.mp4", r"E:\youtube\x", 30.0)
#
# exit()

#
# https://itectec.com/superuser/use-ffmpeg-copy-codec-to-combine-ts-files-into-a-single-mp4/
# 'm not sure why ffmpeg is giving you an error. However ts is one of the few formats that can simply be concatenated. Then, once you have a single ts, transmux to mp4.
#
# Under windows:
#
# copy /b segment1_0_av.ts+segment2_0_av.ts+segment3_0_av.ts all.ts
# ffmpeg -i all.ts -acodec copy -vcodec copy all.mp4