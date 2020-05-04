import math

rna='CACAAUAGCCCGUGCUACCUGUGAAAUUACACGGAGCUUCGGUGGAUACGUUUUCACGAGACGUAGCGCU'

na = rna.count('A')
nc = rna.count('C')

print(math.factorial(na)*math.factorial(nc))
