#######################################################################################################
# indica o caminho dos módulos locais
import sys           
sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
# sys.path.insert(0, "/home/iquanta/Micael/python_modules")

#######################################################################################################
#       													                                          #
#									Módulos importados	        				                      #
#                                   													              #
from numpy import arange, sqrt, zeros
from numpy.random import shuffle

from cascadef import * 
'''
	# cascadef - Módulo contendo funções para implemetnação do protocolo CASCADE
	import customplot as ctp # módulo para padronizar as figuras geradas
	ctp.first_run() # seta variáveis e habilita a exportação do codigo latex. 
	# Deve ser executado antes de qualquer plotagem
'''
snr = 3
ro = sqrt(snr/(snr+1))

ro = 0.9
err = zeros((1,1000), dtype = int)[0]
for i in range(1000):
	a, b, err[i], k = strings(ro, 3, 1000)


# Permutation pattern generation
sig = arange(a.size) 
shuffle(sig) # permutation pattern

ar, br = cascade(a, b, sig, k) 
ar2, br2 = cascade(a, b, sig, k, recur = True) # para utilização de recursividade

