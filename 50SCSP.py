import sys
import array

sys.setrecursionlimit(100000)
import faulthandler; faulthandler.enable()

def trace_alignment(i,J):
	if J[i]=={}:
		return('')
	return(trace_alignment(J[i]['source'],J) + J[i]['base'])


def pretty_print_matrix(M):
	top=' ' + ' ' + seq_t
	side=' ' + seq_s
	print(' '.join(top))
	n=len(seq_s)
	m=len(seq_t)
	for i in range(0,n+1):
		row = [side[i]] + [str(M[i*(m+1)+j]) for j in range(0,m+1)]
		print(' '.join(row))


def pretty_print_indexes():
	top=' ' + ' ' + seq_t
	side=' ' + seq_s
	print(' '.join(top))
	n=len(seq_s)
	m=len(seq_t)
	for i in range(0,n+1):
		row = [side[i]] + [str(i*(m+1)+j) for j in range(0,m+1)]
		print(' '.join(row))

def check_seq(alignment,seq):
	for ai in range(0,len(alignment)):
		c=alignment[ai]
		i = seq.index(c)
		seq=seq[i+1:]
	return(seq)


# fin = open("inputs/50SCSP.txt")
fin = open("inputs/rosalind_scsp.txt")
seqs=[seq.rstrip() for seq in fin.readlines()]


print(seqs)
seq_s,seq_t = seqs



n=len(seq_s) # rows
m=len(seq_t) # columns

nr=n+1
nc=m+1


H = array.array('i', [0]*nr*nc)
J = [{} for j in range(0,(n+1)*(m+1))]


for i in range(1,nr):
	H[i*nc]=-i
	J[i*nc]={'base':seq_s[i-1],'source':(i-1)*nc}

for j in range(1,nc):
	H[j]=-j
	J[j]={'base':seq_t[j-1],'source':j-1}

# pretty_print_matrix(H)
# pretty_print_matrix(J)
# pretty_print_indexes()

highest_score=0
highest_scoring_index=0

for i in range(1,nr):
	for j in range(1,nc):
		s=-1000000 # Mismatch penalty needs to be essentially infinite

		if seq_s[i-1]==seq_t[j-1]:
			s=1

		diag = H[(i-1)*nc+j-1]+s
		gap_down = H[(i-1)*nc+j]
		gap_across = H[i*nc+j-1]

		best_score = max([diag,gap_down,gap_across])
		H[i*nc+j] = best_score
		if best_score==diag:
			J[i*nc+j]={'base':seq_s[i-1],'source':(i-1)*nc+j-1}
		elif best_score == gap_down:
			J[i*nc+j]={'base':seq_s[i-1],'source':(i-1)*nc+j}
		else:
			J[i*nc+j]={'base':seq_t[j-1],'source':i*nc+j-1}		

		if best_score > highest_score:
			highest_scoring_index=i*nc+j



print(seq_s)
print(seq_t)

lcs = trace_alignment(nc*nr-1,J)
print(lcs)
