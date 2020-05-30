import sys
import array

sys.setrecursionlimit(100000)

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

def trace_alignment(i,J):
	if J[i]=={}:
		return([])
	return(trace_alignment(J[i]['source'],J) + [J[i]['base']])

def print_alignment(alignment):
	for i in [0,2]:
		row = [aln[i] for aln in alignment]
		print(''.join(row))


def pretty_print_matrix(M):
	top=' ' + ' ' + seq_t
	side=' ' + seq_s
	print(' '.join(top))
	n=len(seq_s)
	m=len(seq_t)
	for i in range(0,n+1):
		row = [side[i]] + [str(-M[i*(m+1)+j]) for j in range(0,m+1)]
		print(' '.join(row))

def check_seq(alignment,seq):
	for ai in range(0,len(alignment)):
		c=alignment[ai]
		i = seq.index(c)
		seq=seq[i+1:]
	return(seq)


# fin = open("inputs/58EDTA.fasta")
fin = open("inputs/rosalind_edta.txt")
seqs = [seq for name,seq in read_fasta(fin)]
seq_t,seq_s = seqs

n=len(seq_s) # rows
m=len(seq_t) # columns

nr=n+1
nc=m+1


H = array.array('i', [0]*nr*nc)
J = [{} for j in range(0,(n+1)*(m+1))]

for i in range(1,nr):
	H[i*nc]=-i
	J[i*nc]={'base':('-','-',seq_s[i-1]),'source':(i-1)*nc}

for j in range(1,nc):
	H[j]=-j
	J[j]={'base':(seq_t[j-1],'-','-'),'source':j-1}

highest_score=-1000000
highest_scoring_index=0

for i in range(1,nr):
	for j in range(1,nc):
		s=-1 # For anything other than a match

		ss=seq_s[i-1]
		st=seq_t[j-1]

		if ss==st: # For a match
			s=0

		diag = H[(i-1)*nc+j-1]+s
		gap_down = H[(i-1)*nc+j]-1
		gap_across = H[i*nc+j-1]-1

		best_score = max([diag,gap_down,gap_across])
		H[i*nc+j] = best_score
		if best_score==diag:
			if ( s==0):
				J[i*nc+j]={'base':(st,ss,ss),
							'source':(i-1)*nc+j-1}
			else:
				J[i*nc+j]={'base':(st,'*',ss),'source':(i-1)*nc+j-1}
		elif best_score == gap_down:
			J[i*nc+j]={'base':('-','-',ss),'source':(i-1)*nc+j}
		else:
			J[i*nc+j]={'base':(st,'-','-'),'source':i*nc+j-1}		

		if best_score > highest_score:
			highest_scoring_index=i*nc+j

alignment = trace_alignment(highest_scoring_index,J)


# pretty_print_matrix(H)
# print(J)

print(-best_score)

#print(alignment)
print_alignment(alignment)
