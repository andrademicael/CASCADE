#######################################################################################################
# indica o caminho dos móculos locais
import sys           
# sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
sys.path.insert(0, "/home/iquanta/Micael/python_modules")

#######################################################################################################
#       													                                          #
#									Módulos importados	        				                      #
#                                   													              #
from numpy import arange
from numpy.random import shuffle

from cascadef import * 
'''
	# cascadef - Módulo contendo funções para implemetnação do protocolo CASCADE
	import customplot as ctp # módulo para padronizar as figuras geradas
	ctp.first_run() # seta variáveis e habilita a exportação do codigo latex. 
	# Deve ser executado antes de qualquer plotagem
'''

a, b, k, snr = strings(0.96, 2, 1000)

# Permutation pattern generation
sig = arange(a.size) 
shuffle(sig) # permutation pattern

a, b = cascade(a, b, sig, k)

