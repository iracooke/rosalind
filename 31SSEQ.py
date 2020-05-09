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


fin = open("inputs/31SSEQ.fasta")

seqs = [seq for name,seq in read_fasta(fin)]

s=seqs[0]
t=seqs[1]

p=0
sseq=[]
for c in t:
	for i in range(p,len(s)):
		if s[i] == c:
			sseq.append(i+1)
			p=i+1
			break


t_check = ''.join([s[i-1] for i in sseq])
if t_check != t:
	print("Error")
	exit()

print(' '.join(map(str,sseq)))

			