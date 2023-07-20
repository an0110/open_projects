import os
import re
import time
from pprint import pprint
import argparse
from subprocess import Popen

parser = argparse.ArgumentParser(description='')
parser.add_argument('file', help='the file to open links from')
# parser.add_argument('chrome_mode', help='incognito or default')

args = parser.parse_args()
file = args.file
# chrome_mode = args.chrome_mode

models = []
with open (file) as fh:
     data = fh.readlines()

for line in data:
    if line.startswith("#"):
        pass
    else:
        models.append(line)

total_links= len(data)
number_of_lines_to_open = int(len(models)/6)-3 # in one batch
seconds_to_wait = number_of_lines_to_open * 1.2 #1.22 # 1.3 #1.5


print("... opening {} links at once...".format(number_of_lines_to_open))

chrome = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
# chrome = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# if os.path.isfile(chrome):
    # print ("*6"*10)
# else:
    # exit()

pause_timer = 0
for el in models:
    pause_timer += 1
    if pause_timer % number_of_lines_to_open == 0:
        print("... sleepin {} seconds ...".format(seconds_to_wait))
        time.sleep(seconds_to_wait)

    command = chrome + ' --incognito {}'.format(el)
    sts = Popen(command, shell=True).wait()
    time.sleep(0.5)
