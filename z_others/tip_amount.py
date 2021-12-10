import re

# reg = "(\d{1,3})\w.*\n.*\d{1,2}\/\d{1,2}\/\d{1,2}\t(\d{1,2}:\d{1,2})"

file_x = "tips_xxxxx"
file_x = "tips_x2.txt"
with open(file_x,"r") as input:
    read_data = input.readlines()

reg_tip = r"tipped\s(\d{1,3})\stokens\n"


sum = 0
for line in read_data:
    # print (line)
    match_to_capture = re.search(reg_tip, line)
    if match_to_capture:
        sum = sum + int(match_to_capture.group(1))

print("{}  {}".format(sum, sum/20))



