import sys
import functools

def read_fasta(fp):
	name, seq = None, []
	for line in fp:
		line = line.rstrip()
		if line.startswith(">"):
			if name: yield (name, ''.join(seq))
			name, seq = line[1:], []
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))


def n_cat(n):
	if (n==0) or (n==1):
		return(1)
	nc=0

	for k in range(1,n+1):
		nc+=n_cat(k-1)*n_cat(n-k)
		# print(str(k) + ' ' +str(nc) + ' ' + str(n-k))

	return(nc)

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
	if (len(seq) == 0):
		return(1)
	if (len(seq) == 2) and (seq[0] == comp_base(seq[1])): 
		return(1)

	if (len(seq) % 2)!=0:
		print("Error: seq length must be even")
		exit()

	if not has_pairings(seq):
		return(0)

	nc=0
	n=int(len(seq)/2)
	for k in range(1,n+1):
		m=2*k-1

		if seq[0] == comp_base(seq[m]):
			nc_sub=0
			seq_k1 = seq[1:m]
			seq_nk = seq[m+1:]

			if has_pairings(seq_k1) and has_pairings(seq_nk):
				nc_k1=rna_cat(seq_k1)
				if nc_k1>0:
					nc_nk = rna_cat(seq_nk)
					nc_sub=nc_k1*nc_nk
			nc+=nc_sub
	return(nc)




fin = open("inputs/34CAT.fasta")

seqs = [seq for name,seq in read_fasta(fin)]

seq = seqs[0]

print(rna_cat(seq) % 1000000)


