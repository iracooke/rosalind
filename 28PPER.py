import math

n=88
k=9

n_combinations = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print(n_combinations*math.factorial(k) % 1000000)
