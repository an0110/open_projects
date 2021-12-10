import os
from pprint import pprint

pprint ("testing")

def sum13(nums):
  sum = 0
  
  if len(nums) > 0:
    for x in nums:
      sum = sum + x
  else:
    sum = 0
  return sum

  
arr1 = [1, -2, 2, 1, 13]
print ( sum13 (arr1) )

print "-------------------"
arr2 = []
print ( sum13 (arr2) )

