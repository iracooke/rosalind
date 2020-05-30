
dnatrans=str.maketrans("ACTG", "TGAC")
def revc(seq):
	return(seq.translate(dnatrans)[::-1])


# infile="inputs/57DBRU.txt"
infile="inputs/rosalind_dbru.txt"

reads = [line.rstrip() for line in open(infile).readlines()]
rc_reads = [revc(r) for r in reads]


read_set = set(reads+rc_reads)


k=len(reads[0])
for seq in sorted(read_set):
	print("("+seq[0:k-1]+", "+seq[1:k+1]+")")
