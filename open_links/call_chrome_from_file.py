import os
import re
from pprint import pprint
from time import time, sleep

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('file', help='the file to open links from')
# parser.add_argument('chrome_mode', help='incognito or default')

args = parser.parse_args()
file = args.file
# chrome_mode = args.chrome_mode
current_time1 = time()

models = []
with open (file) as fh:
     data = fh.readlines()

for line in data:
    if line.startswith("#"):
        pass
    else:
        models.append(line)

number_of_lines_to_open = 40 # in one batch
seconds_to_wait = number_of_lines_to_open * 1.4

print("... opening {} links at once,...".format(number_of_lines_to_open))

pause_timer = 0
for el in models:
    pause_timer += 1
    if pause_timer % number_of_lines_to_open == 0:
        print("... sleepin {} seconds ...".format(seconds_to_wait))
        sleep(seconds_to_wait)
    #
    # _chrome = "C:\Program Files\Google\Chrome\Application"

    os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" --incognito {}'.format(el))
    # os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --incognito {}'.format(el))

current_time2 = time()
diff = current_time2 - current_time1

pprint ("\n\n\t total time: \n {:.2f} minutes".format((diff/60)))
