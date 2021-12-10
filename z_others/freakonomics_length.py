import re

# reg = "(\d{1,3})\w.*\n.*\d{1,2}\/\d{1,2}\/\d{1,2}\t(\d{1,2}:\d{1,2})"

file_x = "freak.txt"
with open(file_x,"r") as input:
    read_data = input.readlines()


time_list = []

reg_ignore_line = r"^\d{1,3}\w.*\n"
reg_capture_time = r"\d{1,2}\/\d{1,2}\/\d{1,2}\t(\d{1,2}:\d{1,2})"
reg_rebroadcast = r"\(Rebroadcast\)\n"

time = 0
skip = False
for line in read_data:
    match_to_ignore = re.search(reg_ignore_line, line)
    if match_to_ignore:
        match_rebroadcast = re.search(reg_rebroadcast, line)
        if match_rebroadcast:
            skip = True
            pass
        else:
            skip = False
    else:
        if skip == False:
            match_to_capture = re.search(reg_capture_time, line)
            if match_to_capture:
                time_list.append(match_to_capture.group(1) )
                skip = False


for t in time_list:
    (min, sec) = ( int(t.split(":")[0]), int(t.split(":")[0]) )
    min = min + sec/60
    time = time + min


print ("total duration:  {} minutes    or  {} hours".format(time, time/60))



