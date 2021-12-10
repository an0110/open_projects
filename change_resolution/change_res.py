# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture('D:\DOWNLOADS\ISO26262.mp4')
#
# resX = 960
# resY = 540
#
# # resX = 1280
# # resY =
#
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 5, (resX, resY))
#
# while True:
#     ret, frame = cap.read()
#     if ret == True:
#         b = cv2.resize(frame, (resX, resY), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
#         out.write(b)
#     else:
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()


from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *

myclip = VideoFileClip(r'E:\youtube\11\Ultimate Wild Animals Collection in 8K ULTRA HD _ 8K TV.mp4')

final = myclip.fx( vfx.resize, width = 480) #1080      720    480
# final.ipython_display()
final.write_videofile(r"E:\youtube\11\resize_8ktest.mp4")



