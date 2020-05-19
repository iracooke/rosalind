# This solution is based on ideas from Euna Park's Masters Thesis
# https://scholarworks.sjsu.edu/etd_projects/104?utm_source=scholarworks.sjsu.edu%2Fetd_projects%2F104&utm_medium=PDF&utm_campaign=PDFCoverPages
# DOI: https://doi.org/10.31979/etd.qm9e-d3gt

import sys
import itertools
import functools
import multiprocessing

sys.setrecursionlimit(10000)

def generate_rotations(n):
	rotations=[]
	for k in range(2,n):
		rotations.append([(i,i+k-1) for i in range(0,n-k+1)])
	return(rotations)

def apply_rotation(rot,seq):
	i,j=rot
	rseq = seq[:i] + [c for c in reversed(seq[i:j+1])] + seq[j+1:]
	return(rseq)

def all_breaks(s1,s2):
	ps1in2 = [s1.index(c) for c in s2]

	n=len(s1)
	b=[]
	for i in range(0,n-1):
		if abs(ps1in2[i+1] - ps1in2[i]) != 1:
			b.append((i+1,i+2))

	if (ps1in2[n-1] != (n-1)):
		b.append((n,n+1))
	if ps1in2[0] != 0:
		b = [(0,1)] + b
	return(b)

def breakpoint_rotations(bl,s1,s2):
	bp_combinations = itertools.combinations(bl,2)
	breaks=set()
	for bp_pair in bp_combinations:
		p1=bp_pair[0][0]
		p2=bp_pair[1][0]
		if p2 < p1:
			p2=p1
			p1=bp_pair[1][0]
		if(p1==0):
			p1=0
		if(p2==10):
			p2=10
		if(p1!=(p2-1)):
			breaks.add((p1,p2-1))
	return(breaks)

# Recursive search of the reversals tree
#
def best_revs(pair,d=0,	best_depth=10):
	s1=pair[0]
	s2=pair[1]
	if (s1 == s2 ):
		return(d)

	# Avoid searching useless portions of the graph
	d+=1	
	if (d >= best_depth):
		return(100)


	bl = all_breaks(s1,s2)
	bp_rotations = breakpoint_rotations(bl,s1,s2)

	min_nb = 40
	best = []
	for r in bp_rotations:
		s2_rot = apply_rotation(r,s2)
		nb = len(all_breaks(s1,s2_rot))
		if (nb<min_nb):
			min_nb=nb
			best = [(r,s2_rot)]
		elif(nb==min_nb):
			best.append((r,s2_rot))

	progress=0
	for r,s2_rot in best:

		r_d = best_revs((s1,s2_rot),d,best_depth)
		if( r_d < best_depth):
			best_depth=r_d

		if (d == 1):
			progress+=1
			print("Progress : "+str(progress/len(best)))



	return(best_depth)



#fin = open("inputs/42REAR.txt")
fin = open("inputs/rosalind_rear2.txt")

lines=[]
pairs=[]
for line in fin:
	line = line.rstrip().lstrip()
	if line == '':
		s1=lines[0]
		s2=lines[1]
		pairs.append([s1,s2])
		lines=[]
	else:
		line_ints = [int(i) for i in line.split(' ')]
		lines.append(line_ints)
if(lines[0]):
	s1=lines[0]
	s2=lines[1]
	pairs.append([s1,s2])

# We are right on the edge of our 5 minute time limit so 
# use multiprocessing to try and give ourselves the best possible chance
#
ppool = multiprocessing.Pool(5)

rev_dists = ppool.map(best_revs,pairs)

print(' '.join(map(str,rev_dists)))
