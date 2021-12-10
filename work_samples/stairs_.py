#!/bin/python

import math
import os
import random
import re
import sys

def drawx(x,n):
    _line = ""
    for _el in range(n-x):
        _line += " "
    for _el in range(x):
        _line += "#"
	# _line += "\n"
    
    return _line 

	

for _x in range(6):
	print drawx(_x+1,6);