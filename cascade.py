#######################################################################################################
# indica o caminho dos móculos locais
import sys           
#sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
sys.path.insert(0, "/home/iquanta/Micael/python_modules")

#######################################################################################################

from numpy import empty, arange, where, zeros
from numpy.random import shuffle, randint
from commpy import bsc

import ipdb

from cascadef import * # módulo contendo funções para implemetnação do protocolo CASCADE
# import customplot as ctp # módulo para padronizar as ficuras geradas
# ctp.fist_run() # seta variáveis e habilita a exportação do codigo latex. 
#Deve ser executado antes de qualquer plotagem

#######################################################################################################

###################################################
#                                                 #
#		geração das VA's A e B                    #
#                                                 #
###################################################

######################################################################################################
Pe = 0.3 # Channel error probabilitie
k = int(0.73/Pe) # First iteration block size
a = randint(0,2,(1,20))[0] # Alice's string generation
b = bsc(a,Pe) # Bob's string generation (transmission through a BSC Channel woth a Pe error probability)

l = a.size # String size

print('erros nas posições:')
print('%a' % where(a != b))

######################################################################################################
# Permutation pattern generation
sig = arange(l) 
shuffle(sig)
siga = sig.copy() # permutation pattern security copy
######################################################################################################
# CASCADE 1st step
# first strings permutation
a = a[sig]
b = b[sig]
b = dichotomic(a,b,k)[0]
step = 1
######################################################################################################
# 2nd Step
ipdb.set_trace()
while k<l:
	a = a[sig]
	b = b[sig]
	siga = siga[sig]
	k *= 2	
	b, pos = dichotomic(a,b,k)
	step += 1

	if pos.size != 0:
		b = recurs(a, b, pos, sig, siga, k, step)
	
print('')
print('erros restantes após a reconciliação (%i passos): ' % step)
print('%a' % where(a != b))

