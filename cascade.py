#######################################################################################################
# indica o caminho dos móculos locais
import sys           
sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
# sys.path.insert(0, "/home/iquanta/Micael/python_modules")

#######################################################################################################
#       													                                          #
#									Módulos importados	        				                      #
#                                   													              #
from numpy import arange, log10, where, zeros
from numpy.random import shuffle
from scipy.stats import norm
# from commpy import bsc

from cascadef import * 
'''
	# cascadef - Módulo contendo funções para implemetnação do protocolo CASCADE
	import customplot as ctp # módulo para padronizar as figuras geradas
	ctp.first_run() # seta variáveis e habilita a exportação do codigo latex. 
	# Deve ser executado antes de qualquer plotagem
'''

#######################################################################################################
#									Geração das VA's A e B        				                      #
#                                   													              #
'''
	Duas variaveis aleatŕoia são geradas: Gaussianas correlacionadas. As funções cumulativas de 
	probabilidade de suas realizações assumem uma distribuição uniforme (maximizando entropia).
	A partir disto, são geradas expansões em base 2, dado um numero fixo de bits para representação
	dos valores das CDF's
'''
n_r = 100 # quantidade de realizações
media = 0 # média das VAG's
ro = float(input('coeficiente de correlação: '))
sigma = 1 # variância

A, B, var_a, var_b, var_n = cor_var(n_r, media, ro, sigma) # gera as duas VA's Gaussianas correlacionadas
k = int(0.73/var_n) # First iteration block size

snr = 10*log10(var_a/var_n)

cdfa = norm.cdf(A) # valor da CDF para cada valor de A
cdfb = norm.cdf(B) # valor da CDF para cada valor de B

nbits = int(input('quantidade de bits da representação: '))	

s_a = zeros((n_r, nbits), dtype = int)
s_b = zeros((n_r, nbits), dtype = int)
for i in range(n_r):
	s_a[i,:] = b2_exp(cdfa[i],nbits)
	s_b[i,:] = b2_exp(cdfb[i],nbits)

a = s_a.reshape((1,s_a.size))[0]
b = s_b.reshape((1,s_b.size))[0]
l = a.size # String size

print('\nInício da CASCADE. \nParâmetros da simulação: ')
print('\nRealizações: %i ' % n_r)
print('Média e coeficiente de correlação das VA\'s: %.2f, %.2f' % (media, ro))
print('Número de bits para representação: %i' % nbits)
print('Comprimento total das strings: %i' % l)
print('Quantidade de erros gerados: %i ' % where(a != b)[0].size)
print('Variância do ruído: %.2f' % var_n)
print('SRN: %.2f' % snr)
print('Tamanho to bloco: %i' % k)

######################################################################################################
# Permutation pattern generation
sig = arange(l) 
shuffle(sig) # permutation pattern
# print('Padrão de permutação:\n%s' % sig)

######################################################################################################
#									CASCADE 1st Step 			           		                     #
#                                   													             #

# first strings permutation
a = a[sig]
b = b[sig] # a primeira permutação é considerada como posição inicial da cadeia de bits
siga = arange(l) # original bits positions

b, pos = dichotomic(a,b,k) # first search
'''
	pos inform wrong bits positions tha were solved on a not permuted list, e.g, arange(1,l)
	the original solved bits positions rely on siga[pos]
'''
step = 1 # first step compleated
print('')
print('Após o passo %i, restam %i erros a serem corrigidos: ' % (step, where(a != b)[0].size))

######################################################################################################
#									CASCADE 2nd Step 			           		                     #
#                                   													             #
# k *= 2 # double block size
while step<4: # o tamanho do bloco para realizar dichotomic() deve ser menor que o tamanho da string
	a = a[sig] # permutation
	b = b[sig] # permutation
	siga = siga[sig] # keeps the original bits positions by permuting siga
	b, pos = dichotomic(a,b,k) # realize dichotomic() 
	step += 1 # step compleated
	print('')
	print('Após o passo %i, restam %i erros a serem corrigidos: ' % (step, where(a != b)[0].size))
	'''
		if pos.size != 0: # if any error was corrected, must be done a recursive search
			print('Strings antes da recursividade: \nA: \n%s \nB:\n%s' % (a.reshape((n_r, nbits)), b.reshape((n_r, nbits))))
			b = recurs(a, b, siga[pos], sig, k, step)
			print('Strings depois da recursividade: \nA: \n%s \nB:\n%s' % (a.reshape((n_r, nbits)), b.reshape((n_r, nbits))))
		k *= 2 # double block size
	'''
