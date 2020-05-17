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


def dst(s1,s2):
	ndiff=0
	for i,j in zip(s1,s2):
		if i!=j:
			ndiff+=1
	return(ndiff/len(s1))


fin = open("inputs/rosalind_pdst.txt")

seqs = [seq for name,seq in read_fasta(fin)]


for s1 in seqs:
	rowd = ['{0:0.5f}'.format(dst(s1,s2)) for s2 in seqs]
	print(' '.join(rowd))


