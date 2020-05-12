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


fin = open("inputs/rosalind_kmer.txt")
seqs = [seq for name,seq in read_fasta(fin)]
seq = seqs[0]

def all_kmers(k):
	if k==1:
		return(dna_alphabet)

	all_suff=all_kmers(k-1)
	all=[]
	for c in dna_alphabet:
		cs = [c+s for s in all_suff]
		all = all + cs
	return(all)


dna_alphabet = ['A','C','G','T']

all_4mers = all_kmers(4)

all_inseq = [seq[i:i+4] for i in range(0,len(seq)-3)]

# print(seq)
# print(len(seq)-3)
# print(len(all_inseq))
# print(all_inseq)

#import pdb;pdb.set_trace()

#composition = [seq.count(kmer) for kmer in all_4mers]
#print(composition)

composition = [all_inseq.count(kmer) for kmer in all_4mers]

print(' '.join(map(str,composition)))