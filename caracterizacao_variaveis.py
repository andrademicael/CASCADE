import sys           
# sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
sys.path.insert(0, "/home/iquanta/Micael/python_modules")
from numpy import zeros, arange
from cascadef import strings
import customplot as ctp 
ctp.first_run()
import matplotlib.pyplot as plt

ordem = 6 # ordem da expansão
snr = arange(11) # valor máximo da snr
n_re = 1000 # número de realizações das VA's
n_r = 10000 # numero de repetições do experimento
m_e = zeros((snr.size,ordem))

for i in snr:
	sume = zeros((1,ordem))[0]
	for t in range(n_r):
		a, b, err = strings(i, ordem, n_re, display = True)
		sume += err/n_r # calcula a média de erros e cada repetição do experimento
	m_e[i,:] = sume/n_re # calcula a porcentagem de erros gerada para cada valor de SNR em cada canal

fig = ctp.newfig(0.8)
for k in range(ordem):
	plt.plot(snr, m_e[:,k], label = 'Canal %i' % (k+1))

plt.xlabel(r'SNR')
plt.ylabel(r'Porcentagem de bits errados')
plt.title('Porcentagem de erros gerados por canal')
plt.legend(loc='lower left')
ctp.savefig('erro')
