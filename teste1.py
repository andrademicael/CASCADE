from cascadef import *
from numpy.random import randint
from numpy import asarray, zeros
#import ipdb
t = 21
x = zeros((1,t), dtype = int)[0]

y = x.copy()
r = randint(0,t)
y[r] = (y[r] + 1) % 2

print('string x:')
print(x)

print('string y:')
print(y)

y = binary(x,y)
print('string y reconciliada')
print(y)




