#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    _minArr = 0
    _maxArr = 0
    _sumArr = 0

    _outMax = 0
    _outMin = 0

    for _el in arr:
        if _el < _minArr:
            _minArr = _el
        if _el > _maxArr:
            _maxArr = _el
        
        _sumArr += _el
	
	print _sumArr, _minArr, _maxArr
	
    _outMax = _sumArr - _minArr
    _outMin = _sumArr - _maxArr

    return str(_outMin) + " " + str(_outMax)

	
print miniMaxSum([1,3,5,7,9])