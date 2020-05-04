import sys,math



# seq='ACGATACAA'
# A='0.129 0.287 0.423 0.476 0.641 0.742 0.783'.split(" ")

seq='CGTTTCACATCCTTAGCGCAGAATGGGCAGTAACCGTGTTTTCGGAATAGGGCTGGGGATACGTTAGAGAACTAAGTCCGGAGAGCTAAC'
A='0.091 0.136 0.197 0.292 0.325 0.383 0.444 0.525 0.600 0.663 0.745 0.792 0.840 0.927'.split(" ")


def get_prob(seq,gc):
	prob = 0
	for c in seq:
		if c in ['A','T']:
			prob += math.log10((1-gc)/2)
		else:
			prob += math.log10(gc/2)
	return(prob)

probs = [get_prob(seq,float(gc)) for gc in A]

print(' '.join(["{0:0.3f}".format(i) for i in probs]))

	