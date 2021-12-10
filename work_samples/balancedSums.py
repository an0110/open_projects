import math
import os
import random
import re
import sys

from pprint import pprint

def sumArr (arr):
	_result = ""
	for _iter in range(len(arr)):
		_sumL = sum(arr[:_iter])
		_sumR = sum(arr[_iter+1:])
		
		if _sumL == _sumR:
			return "YES"
			break
	else:
		return  "NO"

	# return _result
    # Complete this function
    # if len(arr) == 1:
        # return "YES"
    # for i in range(1, int(len(arr)+1/2)):
        # left = sum(arr[:i])
        # right = sum(arr[i+1:])
        # if left == right:
            # return "YES"
            # break
    # else:
        # return "NO"
	# for key, value in _dictOfSums.items():
		# print value
		# if value[0] == value[1]:
			# print key, value[0]
	
	
# Complete the balancedSums function below.
def balancedSums(arr):
	_leftSum  = 0
	_rightSum = 0

	for _iter in range(len(arr)):
		_leftSum += arr[_iter]
		
		_rightSum += arr[-_iter-1]
	
		print _leftSum, _rightSum 
	return 0

if __name__ == '__main__':
	_arr1 = [1, 1, 4, 1, 1]
	_arr2 = [1, 1, 4, 14, 1]
	_arr3 = [1, 1, 4, 1, 1]
	# # sumArr(_arr1)
	print sumArr(_arr3)
	# print balancedSums(_arr2)
	# print  balancedSums(_arr1)
 
 
 
	