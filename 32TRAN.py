import sys

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


fin = open("inputs/32TRAN.fasta")

seqs = [seq for name,seq in read_fasta(fin)]

s1=seqs[0]
s2=seqs[1]

salign = zip(s1,s2)

n_transitions=0
n_transversions=0

for c1,c2 in salign:	
	if c1 != c2:
		mut=c1+c2
		if (mut=='AG') or (mut=='GA') or (mut=='CT') or (mut=='TC'):
			n_transitions+=1
		else:
			n_transversions+=1

print(n_transitions/n_transversions)


