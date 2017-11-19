#from numpy.random import randint, shuffle
from numpy import asarray
#from numpy import arange
#from commpy import bsc
from cascadef import *

# n = 32
# x = randint(0,2,(1,n))[0]
# p_e = 0.15
# y = bsc(x,p_e)

a = asarray([1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0])
b = asarray([1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0])

print('string A')
print(a)
print('string B')
print(b)

n#sig = arange(16)
#shuffle(sig)
sig = [1, 12,  7, 13,  8, 9, 5, 4, 11,  2,  3,  0,  6, 14, 10, 15]
print('permitação, n = 16')
print(sig)