import math

mass_table={}

with open("inputs/monoisotopic_mass_table.txt") as f:
	for line in f:
		aa,mass = line.split()
		mass_table[float(mass)]=aa

# infile="inputs/59FULL.txt"
infile="inputs/rosalind_full.txt"

L = [float(line.rstrip()) for line in open(infile).readlines()]


parent = L[0]
ions = sorted(L[1:])

unpaired_ions = ions.copy()


prefixes=[]
suffixes=[]

i1=unpaired_ions[0]
prefixes.append(i1)
unpaired_ions.remove(i1)

s1=unpaired_ions[-1]
suffixes.append(s1)
unpaired_ions.remove(s1)



while len(unpaired_ions)>0:

	# Find the next prefix ion
	for ion in unpaired_ions:
		mass_diff = abs(round(ion-prefixes[-1],5))
		if mass_table.get(mass_diff)!=None:
			prefixes.append(ion)
			for yi in unpaired_ions:
				d = (yi+ion) - parent
				if ( abs(d) < 0.0001):
					suffixes.append(yi)
					unpaired_ions.remove(yi)
					unpaired_ions.remove(ion)
					break;
			break;

pairs = [(p,s) for p,s in zip(sorted(prefixes),reversed(sorted(suffixes)))]

bseq=""
for i in range(1,len(pairs)):
	pi = pairs[i]
	prev = pairs[i-1]
	db = round(pi[0]-prev[0],5)
	dy = round(prev[1]-pi[1],5)

	baa = mass_table[db]
	yaa = mass_table[dy]

	if(baa != yaa):
		print("Matching error")
		exit()
	else:
		bseq+=baa


print(bseq)





