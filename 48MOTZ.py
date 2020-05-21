import sys
import functools

def comp_base(b):
	if b=='A':
		return('U')
	if b=='U':
		return('A')
	if b=='C':
		return('G')
	if b=='G':
		return('C')
	print("Error")

def has_pairings(seq):
	na = seq.count('A')
	nu = seq.count('U')
	nc = seq.count('C')
	ng = seq.count('G')

	if (na != nu) or (nc != ng):
		return(False)
	return(True)


@functools.lru_cache(maxsize=None) # A crucial speed improvement
def rna_cat(seq):
	if (len(seq) == 0) or (len(seq) == 1):
		return(1)

	if (len(seq) == 2) and (seq[0] == comp_base(seq[1])): 
		return(2)


	b1=seq[0]

	match_indices = [i for i in range(0,len(seq)) if seq[i]==comp_base(b1)]
	nc=rna_cat(seq[1:])
	for k in match_indices:
		left=seq[1:k]
		right=seq[k+1:]
		nc+=rna_cat(left)*rna_cat(right)
	return(nc)


seq='GAUUCUACAGAGUAGGGGAGAAUAAACGAACAGACAGGCAAAUUUAGUUUGCAUGAACACACCAUGAAGCGAGGUGCCUACCUAAAACUGGGACUAUACCGCAGUAACCACGCCGUAGUCUCGAUUCACGGGGCUAUCUAAAAGAUAGUAUUGAAGGCCCUUGGAGCGAGCCCGUAAUCACAAUAUCCCUAUGAGGCUCGCGACCCGGUGGGGCGAACCUAACGUAUAUACGGUGACAACUAUUUAUGUGGAACUAACAUUCCGGAGACUCCAAA'

print(rna_cat(seq) % 1000000)


