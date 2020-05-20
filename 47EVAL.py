# n=10
# s='AG'
# A=map(float,'0.25 0.5 0.75'.split(' '))

n=864193
s='ACCAGTTTT'
A='0.000 0.064 0.142 0.236 0.300 0.367 0.415 0.470 0.528 0.621 0.661 0.690 0.802 0.863 0.882 1.000'
A=map(float,A.split(' '))





k=len(s)

nk = n-k+1

B=[]
for gc in A:
	probs = {'A':(1-gc)/2,'T':(1-gc)/2,'G':gc/2,'C':gc/2}
	ps = 1
	for c in s:
		ps=ps*probs[c]
	B.append(ps*nk)

print(' '.join(map('{0:0.4f}'.format,B)))