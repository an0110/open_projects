import re
from pprint import pprint


_string = "abc def ab 3333]"

_res = re.findall ("ab\s(\d)*]", _string)

pprint (_res)

# print "---------------"
# _res = re.findall ("abe", _string)

# pprint (_res[0])