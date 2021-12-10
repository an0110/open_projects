import threading
import os
from time import sleep
from concurrent import futures
import gc


def write_file(file):
    with open (file, "a+") as fh:
        fh.write("TEST TEST TEST")

    check_(file)

from time import  sleep



def check_(file):
    if os.path.getsize(file) > 10:
        print ("{} bigger than 1 kb".format(file))
    gc.collect()
    if os.path.getsize(file) > 15:
        print ("EXIT")
        exit()


files = ["J:/threads/ab2c.txt", "J:/threads/ge2f.txt"]

ex = futures.ThreadPoolExecutor(max_workers=3)

while True:
    results = ex.map(write_file,files)

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
