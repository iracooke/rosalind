import math

mass_table={}

with open("inputs/monoisotopic_mass_table.txt") as f:
	for line in f:
		aa,mass = line.split()
		mass_table[aa]=float(mass)

spectrum = []

with open("inputs/rosalind_spec.txt") as f:
	spectrum = [float(line.rstrip()) for line in f]
	spectrum = sorted(spectrum)

def mass2aa(m,mass_table):
	for aa,mass in mass_table.items():
		if abs(m-mass)<0.0001:
			return(aa)
	return(None)

# print(mass_table)
# print(spectrum)

mass_diffs = []
for i in range(1,len(spectrum)):
	mass_diffs.append(spectrum[i]-spectrum[i-1])

prot = [mass2aa(d,mass_table) for d in mass_diffs]

print(''.join(prot))