import math

# This uses the // operator to ensure integer division, thereby avoiding overflow errors
def nchoosek(n,k):
	return(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))

# n=6
# m=3
n=1620
m=895



s=0
for k in range(m,n+1):
	print(k)
	s+=nchoosek(n,k)

print(s % 1000000)

