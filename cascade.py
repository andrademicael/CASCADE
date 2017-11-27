#######################################################################################################
# indica o caminho dos móculos locais
import sys           
sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
#sys.path.insert(0, "/home/iquanta/Micael/python_modules")

#######################################################################################################
#       													                                          #
#									Módulos importados	        				                      #
#                                   													              #
from numpy import arange, where, zeros
from numpy.random import shuffle
from scipy.stats import norm
# from commpy import bsc
import ipdb
#ipdb.set_trace()
from cascadef import * 
# cascadef - Módulo contendo funções para implemetnação do protocolo CASCADE
import customplot as ctp # módulo para padronizar as figuras geradas
ctp.first_run() # seta variáveis e habilita a exportação do codigo latex. 
# Deve ser executado antes de qualquer plotagem

#######################################################################################################
#									Geração das VA's A e B        				                      #
#                                   													              #
'''
	Pe = 0.3 # Channel error probabilitie
 
	a = randint(0,2,(1,20))[0] # Alice's string generation
	b = bsc(a,Pe) # Bob's string generation (transmission through a BSC Channel woth a Pe error probability)
'''
'''
	Duas variaveis aleatŕoia são geradas: Gaussianas correlacionadas. As funções cumulativas de 
	probabilidade de suas realizações assumem uma distribuição uniforme (maximizando entropia).
	A partir disto, são geradas expansões em base 2, dado um numero fixo de bits para representação
	dos valores das CDF's
'''
n_r = 6 # quantidade de realizações
media = 0 # média das VAG's
ro = 0.96 # coeficiente de correlação
sigma = 1 # variância
#k = int(0.73/(1-ro)) # First iteration block size
A, B = cor_var(n_r, media, ro, sigma) # gera as duas VA's Gaussianas correlacionadas
k = 6

cdfa = norm.cdf(A) # valor da CDF para cada valor de A
cdfb = norm.cdf(B) # valor da CDF para cada valor de B

nbits = 6 #quantidade de bits da representação
s_a = zeros((n_r, nbits), dtype = int)
s_b = zeros((n_r, nbits), dtype = int)
for i in range(n_r):
	s_a[i,:] = b2_exp(cdfa[i],nbits)
	s_b[i,:] = b2_exp(cdfb[i],nbits)

a = s_a.reshape((1,s_a.size))[0]
b = s_b.reshape((1,s_b.size))[0]
l = a.size # String size

######################################################################################################
# Permutation pattern generation
sig = arange(l) 
shuffle(sig) # permutation pattern
print('Padrão de permutação:\n%s' % sig)

######################################################################################################
#									CASCADE 1st Step 			           		                     #
#                                   													             #
# first strings permutation
a = a[sig]
b = b[sig]
s_a = a.reshape((n_r, nbits))
s_b = b.reshape((n_r, nbits))
siga = arange(l) # original bits positions

print('Sequencias de bits geradas: \nA: \n%s \nB:\n%s' % (s_a, s_b))
print('Foram gerados %i erros nas posições: \n%s' % (where(a != b)[0].size, where(a != b)[0]))
# at this point, a and b bit string follow sig pattern but it will be considered the initial state

b, pos = dichotomic(a,b,k) # first search
# pos inform wrong bits positions tha were solved on a not permuted list, e.g, arange(1,l)
# the original solved bits positions rely on siga[pos]
step = 1 # first step compleated
print('No passo %i foram corrigidos %i erros nas posições: \n%s' % (step, pos.size, siga[pos]))
print('Chave reconciliada até então: \nA: \n%s \nB:\n%s' % (a.reshape((n_r, nbits)), b.reshape((n_r, nbits))))

######################################################################################################
#									CASCADE 2nd Step 			           		                     #
#                                   													             #
#ipdb.set_trace()
while k<l: # o tamanho do bloco para realizar dichotomic() deve ser menor que o tamanho da string
	a = a[sig] # permutation
	b = b[sig] # permutation
	siga = siga[sig] # keeps the original bits positions by permuting siga
	k *= 2 # double block size
	b, pos = dichotomic(a,b,k) # realize dichotomic() 
	step += 1 # step compleated
	print('No passo %i foram corrigidos %i erros nas posições: \n%s' % (step, pos.size, siga[pos]))
	print('Chave reconciliada até então: \nA: \n%s \nB:\n%s' % (a.reshape((n_r, nbits)), b.reshape((n_r, nbits))))
	if pos.size != 0: # if any error was corrected, must be done a recursive search
		b = recurs(a, b, siga[pos], sig, k, step)
	
	# when k >= l, CASCADE has finished and all correctible erros have been treated.

print('')
print('erros restantes após a reconciliação (%i passos): ' % step)
print('%a' % where(a != b))

