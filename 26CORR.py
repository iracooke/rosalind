import sys, math


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

def comp(base):
	dnadict = {'A':'T','T':'A','C':'G','G':'C'}
	return(dnadict[base])

def revcomp(seq):
	return(''.join([comp(s) for s in seq[::-1]]))


def hamm(r1,r2):
	d=0
	for i,j in zip(r1,r2):
		if(i != j):
			d+=1
	return(d)


fin = open("inputs/rosalind_corr.txt")

seqs = [seq for name,seq in read_fasta(fin)]

unique_seqs = {}

for s in seqs:
	rs = revcomp(s)
	if s in unique_seqs:
		unique_seqs[s]['count']+=1
	elif rs in unique_seqs:
		unique_seqs[rs]['count']+=1
	else:
		unique_seqs[s] = {'count':1}

# import pdb;pdb.set_trace()

bad_reads = [s for s in unique_seqs if unique_seqs[s]['count'] == 1]
good_reads = [s for s in unique_seqs if unique_seqs[s]['count'] > 1]

fout = open("outputs/corr.txt","w+")

for br in bad_reads:
	for gr in good_reads:
		if hamm(br,gr)==1:
			fout.write(br + "->" + gr+'\n')
			break;

for br in bad_reads:
	br_rc = revcomp(br)
	for gr in good_reads:
		if hamm(br_rc,gr)==1:
			fout.write(br + "->" + revcomp(gr)+'\n')
			break;

