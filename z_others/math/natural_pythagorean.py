# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math
from math import sqrt


a = 1
b = 1
c = 1
d = b*b + c*c
sum = 1000



for a in range (1, int(sqrt(sum))):
    list = []
    d = sum - a*a

    # print("*" * 10)
    for b in range(1, int(sqrt(d))):

        aux = b*b + a*a
        aux2 = sum-aux
        if sqrt(aux2).is_integer():
            # print (aux2)
            list.append ((sqrt(d), sqrt(aux), sqrt(aux2)))

from pprint import pprint
pprint(list)