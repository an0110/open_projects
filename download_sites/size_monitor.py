import logging
import shutil
import ctypes
from time import sleep, time
from os import listdir,remove
from os.path import isfile, join


disk_limit_alarm = 4*(1024**3)
destination = r"C:\DOWNLOADS\yt_cb_out\full_j_drive"

previous_size = 0

#currewnt time
time0 = time()

log_file = "E:\cb_scheduler.log"
log_format = "[MON]%(asctime)s %(levelname)s: %(message)s"

sleep_time = 30

while True:
    try:
        if isfile(log_file):
            pass
        else:
            ctypes.windll.user32.MessageBoxW(0, "SD card was removed", "WARNING", 0)
    except FileNotFoundError:
        print("errrr ")

    to_inspect = "E:/"
    drive_name = to_inspect[0:2]
    size = shutil.disk_usage(drive_name)[2]

    logging.basicConfig(filename=log_file, filemode='a+', format=log_format, level=logging.DEBUG)

    if size == previous_size :
        pass
    else:
        print ("{:.2f}".format(size/1024**2))
        previous_size = size

    if size < disk_limit_alarm:
        logging.info ("EXITING because of size limit execeded (alarm set at {})".format(disk_limit_alarm))
        # exit()

    ## move mp4 file to HDD
    downloading = []
    onlyfiles = [f for f in listdir(to_inspect) if isfile(join(to_inspect, f))]
    for file in onlyfiles:
        # print(file)
        # create the semaphor file
        if file.endswith(".part"):
            downloading.append( file.split(" ")[0] )

        if file.endswith(".mp4"):

            logging.info ("moving {} to {}".format(file, join(destination,file)))
            shutil.move(join(to_inspect, file), join(destination, file))
            sleep(2)
            logging.info ("------move done-----")

    if len(downloading) > 0:
        print (downloading)
        if len(downloading) > 3:
            logging.info ("\t ----------------------------- \n\t WARNING!!!! more than 4 paralel downloads")
    sleep(sleep_time)

   