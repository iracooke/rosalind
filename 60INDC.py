from math import *

def binomial(k,n):
	return(factorial(n)/(pow(2,n)*(factorial(k)*factorial(n-k))))
n=41

Bk = [binomial(k,2*n) for k in range(1,2*n+1)]

A = ['{0:0.4f}'.format(log10(sum(Bk[k:]))) for k in range(0,2*n)]


print(' '.join(A))

