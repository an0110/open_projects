import threading
import os
from time import sleep
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError

from concurrent import futures



def download_cb(link):
    out_path_ = "J:/out2/"
    opt_format = 'worstaudio/worst'  # 'worstaudio/worst'
    ydl_opts = {'format': opt_format,
                'outtmpl': '{}/%(title)s.%(ext)s'.format(out_path_),
                # "test": "true",
                }

    ydl = YoutubeDL(ydl_opts)
    try:
        ydl.download([link])
    except DownloadError:
        print(" download fail")

names = ["https://chaturbate.com/deya_divine", "https://chaturbate.com/mia__ferrer"]
ex = futures.ThreadPoolExecutor(max_workers=3)

results = ex.map(download_cb, names)

print (results)




exit()

#
# for model_name in names:
#     link = "https://chaturbate.com/" + model_name
x = threading.Thread(target=download_cb("https://chaturbate.com/cellardoor_"))
x.start()

y = threading.Thread(target=download_cb("https://chaturbate.com/beniceandhug"))
y.start()

# z = threading.Thread(target=download_cb(link))
# z.start()



# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#
#
#
#     # Start the load operations and mark each future with its URL
#     future_to_url = {executor.submit(download_cb, link, 60): link for url in URLS}
#
#
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         download_cb(link)
#
#
# for model_name in names:
#     link = "https://chaturbate.com/" + model_name
#
#
