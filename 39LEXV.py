import sys

# Inputs
alphabet=[' ']+'C D Q Y G K U F H I N'.split(' ')

n = 3


def all_kmers(k,dna_alphabet):
	if k==1:
		return(dna_alphabet)

	all_suff=all_kmers(k-1,dna_alphabet)
	all=[]
	for c in dna_alphabet:
		cs = [c+s for s in all_suff]
		all = all + cs
	return(all)

# Lexicographic ordering
# If a string is a prefix of another string it has a higher ordering by virtue of being shorter
# Ordering is based on the first letter of difference

# print(alphabet)

allk = all_kmers(n,alphabet)

# for mer in allk[1:]:
# 	space_i = mer.find(' ')
# 	if space_i==-1:
# 		print('.'+mer+'.')
# 	elif mer[space_i:].replace(' ','') == '':
# 		print('.'+mer+'.')


for mer in allk[1:]:
	space_i = mer.find(' ')
	if space_i==-1:
		print(mer)
	elif mer[space_i:].replace(' ','') == '':
		print(mer)
