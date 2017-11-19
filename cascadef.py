#função para calculo de paridade de uma string binária

def bitpar(s):
	from numpy import sum
	
	par = sum(s) % 2

	return par

#função BYNARY proposta por Brassard e Salvail,
#realiza a correção de um erro entre duas strings a e b
#retorna a string b com um erro corigido e a posição do 
#erro na string

def binary(a,b):
	if bitpar(a) == bitpar(b):
		return b
	else:		
		l = a.size
		k1 = 0
		while l>1:
			if l % 2 == 0:
				if bitpar(a[k1:k1+int(l/2)]) == bitpar(b[k1:k1+int(l/2)]):
					l = int(l/2)
					k1 = k1+l
				else:
					l = int(l/2)
			else:
				if bitpar(a[k1:k1+(int(l/2)+1)]) == bitpar(b[k1:k1+(int(l/2)+1)]):
					l = int(l/2)+1
					k1 = k1+l
				else:
					l = int(l/2)+1				
		b[k1] = (b[k1] + 1) % 2

		return (b, k1)


#Recebe um vetor 'a' tipo inteiro que representa uma permutação qualquer
#e retorna m vetor 'ip' que realiza uma permutação inversa a 'a'

def inv_perm(a):
	from numpy import empty

	ip = empty(a.shape, dtype = int)
	k = 0
	for i in a:
		ip[i] = k
		k += 1
	return ip


if __name__ == '__bitpar__':
	bitpar()
elif __name__ == '__binary__':
	binary()
elif __name__ == '__inv_perm__':
	inv_perm()