import sys,math
import itertools


def permute(items):
	if len(items) == 2:
		return([items,items[::-1]])

	perms = []
	for item in items:
		remaining = items.copy()
		remaining.remove(item)
		perms = perms + [ [item] + p_remain for p_remain in permute(remaining)]

	return(perms)

def flatten(list_of_lists):
	flattened = [val for sublist in list_of_lists for val in sublist]
	return(flattened)

def signings(items):
	sgn=[]
	sgn.append(items)
	indices=list(range(0,len(items)))
	for n in range(1,len(items)+1):
		for comb in itertools.combinations(indices,n):
			signed_items = items.copy()
			for ni in comb:
				signed_items[ni] = -signed_items[ni]
			
			sgn.append(signed_items)
	return(sgn)



n=4

num_signings = math.factorial(n)*math.pow(2,n)

print(num_signings)

items = list(range(1,n+1))


all_signings = flatten([ signings(perm_items) for perm_items in permute(items)])

if (len(all_signings) != num_signings):
	print("Error")
	exit()


for s in all_signings:
	print(' '.join(map(str,s)))
