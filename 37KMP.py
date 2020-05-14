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


fin = open("inputs/rosalind_kmp.txt")
#fin = open("inputs/37KMP.fasta")
seqs = [seq for name,seq in read_fasta(fin)]
seq = seqs[0]


def widest_border(seq,P):
	k=len(seq)
	if k==1:
		return(0)

	extension=seq[-1]
	j=len(P)-1
	while j>=0:
		w=P[j]
		if seq[w]==extension:
			return(w+1)
		else:
			j=P[j]-1

	return(0)

prefix_matches = []

P=[]
for k in range(1,len(seq)+1):
	P.append(widest_border(seq[0:k],P))


print(' '.join(map(str,P)))
