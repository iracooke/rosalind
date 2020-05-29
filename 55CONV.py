from itertools import product

# input="inputs/55CONV.txt"
input="inputs/rosalind_conv.txt"

with open(input) as f:
	multisets=[line.rstrip().split() for line in f]

ms1=map(float,multisets[0])
ms2=map(float,multisets[1])



def minkowski_diff(s1,s2):
	return([round(p[0]-p[1],5) for p in product(s1,s2)])


md = minkowski_diff(ms1,ms2)


multiplicities = {}
for mass in md:
	mm = multiplicities.get(mass,0) +1
	multiplicities[mass]=mm


max_multiplicity=0
best_shift=0
for k,v in multiplicities.items():
	if v>max_multiplicity:
		max_multiplicity=v
		best_shift=k
		
print(max_multiplicity)
print(best_shift)
