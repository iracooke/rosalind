import sys
from collections import Counter
import functools

sys.setrecursionlimit(100000)

def scan_merge(parent,seq_a,seq_b):
	ml=len(seq_a)+len(seq_b)
	pl=len(parent)
	if(ml>pl):
		return(0)

	m_counter=Counter(seq_a+seq_b)

	for i in range(0,pl-ml+1):
		subseq=parent[i:i+ml]
		if len(Counter(subseq)-m_counter)==0:
			if(can_merge(subseq,seq_a,seq_b)):
				return(1)

	return(0)

@functools.lru_cache(maxsize=None)
def can_merge(parent,seq_a,seq_b):

	if (parent==seq_a+seq_b) or (parent==seq_b+seq_a):
		return(True)

	if len(seq_a)>0 and (seq_a[-1] == parent[-1]):
		cm_a = can_merge(parent[:-1],seq_a[:-1],seq_b)
		if len(seq_b)>0 and (not cm_a and seq_b[-1]==parent[-1]):
			return(can_merge(parent[:-1],seq_a,seq_b[:-1]))
		else:
			return(cm_a)

	elif len(seq_b)>0 and (seq_b[-1] == parent[-1]):
		return(can_merge(parent[:-1],seq_a,seq_b[:-1]))


	return(False)

		


# fin = open("inputs/61ITWV.txt")
fin = open("inputs/rosalind_itwv.txt")
seqs = [line.rstrip() for line in fin.readlines()]
parent_seq = seqs[0]

seqs=seqs[1:]

for sa in seqs:
	row = [scan_merge(parent_seq,sa,sb) for sb in seqs]
	print(' '.join(map(str,row)))

