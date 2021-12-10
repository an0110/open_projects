#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	# a = a.strip(lower(a) )
	# b = strip(lower(b))
	_numbers = 0
	a = "".join(sorted(a))
	b = "".join(sorted(b))
	
	print a
	print b
	
	print "~~~~~~~~~~~~~~~~~"
	
	if a in b:
		_numbers = 0
	else:
		if len(a) <= len(b):
			for _i in range(len(a)):
				print a[_i:]
				if a[_i:] in b:
					print "~~a"
					_numbers = _i 
					break
				else:
					continue
		else:
			pass

	# _numbers = 1
	
		
	return _numbers
	
	# bacdc
	# dcbac 


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a = raw_input()

    # b = raw_input()

    # res = makeAnagram(a, b)

    # fptr.write(str(res) + '\n')

    # fptr.close()

	
	a = "eabc"
	b = "cdeagb"
	
	res = makeAnagram(a, b)
	
	print res