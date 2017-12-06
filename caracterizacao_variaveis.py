import sys           
sys.path.insert(0, "/home/micael/Dropbox/MESTRADO/Mestrado-Micael-2017-1/Algoritmos/python_modules")
from numpy import zeros
from cascadef import strings
import customplot as ctp 
ctp.first_run()
import matplotlib.pyplot as plt

nb = 6
snr = 10
sume = 0
n_r = 100
p_e = zeros((snr+1,nb))

for j in range(1, nb+1):
	for i in range(snr+1):
		sume = 0
		for t in range(n_r):
			a, b, err, k = strings(i, j, 1000, display = False)
			sume += err/n_r
		p_e[i,j-1] = sume/(1000*j)

fig = ctp.newfig(0.8)
for k in range(nb):
	plt.plot(range(snr+1), p_e[:,k], label = 'nb = %i' % (k+1))

plt.xlabel(r'SNR')
plt.ylabel(r'Número médio de erros')
plt.title('Número médio de erros para nb = {1, 2, 3, 4, 5, 6}')
plt.legend(loc='upper right')
ctp.savefig('erro_medio')
