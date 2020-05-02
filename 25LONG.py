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


def print_fasta(name,seq):
	sys.stdout.write(">"+name+"\n"+seq+"\n")

# Returns none if they don't overlap
# Returns the new joined string and overlap length if they do
def max_overlap(seq1,seq2,min_overlap):
	max_sp=0
	max_ps=0
	ls1=len(seq1)
	ls2=len(seq2)

	# Check suffix of seq1 against prefix of seq2
	for sl in range(1,min(ls1,ls2)):
		suff=seq1[ls1-sl:ls1]
		pref=seq2[0:sl]
		if suff==pref:
			max_sp=sl


	# Check suffix of seq2 against prefix of seq1
	for sl in range(1,min(ls1,ls2)):
		suff=seq2[ls2-sl:ls2]
		pref=seq1[0:sl]
		if suff==pref:
			max_ps=sl

	overlap = max(max_ps,max_sp)
	if overlap < min_overlap:
		return([None,0])

	if max_sp>max_ps:
		ss = seq1 + seq2[max_sp:ls2]
	else:
		ss = seq2 + seq1[max_ps:ls1]
	return([ss,overlap])




fin = open("inputs/rosalind_long.txt")

seqs = [seq for name,seq in read_fasta(fin)]

originals = seqs

min_overlap = int(math.floor(len(min(seqs, key = len))/2))


def best_pair(seqs):
	best_o = 0
	result=[]
	for i in range(0,len(seqs)):
		for j in range(i+1,len(seqs)):
			mo = max_overlap(seqs[i],seqs[j],min_overlap)
			if ( mo[1] > best_o):
				best_o = mo[1]
				result=[i,j,mo[0]]
	if ( best_o == 0):
		import pdb;pdb.set_trace()
		print("Error: No best pair")

	return(result)

# Check to see if there are any seqs contained in others
inner_seqs = []
for i in range(0,len(seqs)):
	for s in seqs:
		if ( s in seqs[0] and (s!=seqs[0])):
			inner_seqs.append(s)
for s in inner_seqs:
	seqs.remove(s)

# Perform greedy assembly
#
while len(seqs) > 1:
	print(len(seqs))
	bp = best_pair(seqs)
	seqs[bp[1]]=bp[2]
	seqs.pop(bp[0])

chrom = seqs[0]

# Check that the final result contains all the reads
for s in originals:
	if not (s in chrom):
		print("Not in chromosome")

print(chrom)