# Note:  To get the correct answer this has to be run with python2.7 as the answer online includes python2.7 numerical approximations.

import math
seq='AUGCUUC'


#seq='GAGCGUCGGCCAUGAUGGUGCACAGUGUUACAGCGGAGACGCAGGCAAGUUGCCUGUGCGGUCGGCUAGUGUUCUGGGAUGUACGGCUG'

seq='AAGGCUCCCAGGAUAGCUUCUACUACAAACUAGCACGAAUAGGGUGGUAGCUAAUGGGUCGUAAAGAGCAUUAGCCUCCUACACCUGC'

seq='AAUUCGUGUCGUGGGGCUAAGGAACAAAGGAUUUGUUGGCAUGUAUCCAAAGGUCUUCAGGAGGUAGACCCCACCUAAAGCUCCGGUACCAGACC'

na = seq.count('A')
nu = seq.count('U')
nc = seq.count('C')
ng = seq.count('G')

if (na+nu+nc+ng) != len(seq):
	print("Error")
	exit()

m_au = max(na,nu)
n_au = min(na,nu)

m_cg = max(nc,ng)
n_cg = min(nc,ng)

print(m_au,n_au,m_cg,n_cg)

au_mm = math.factorial(m_au)/math.factorial(m_au-n_au)
cg_mm = math.factorial(m_cg)/math.factorial(m_cg-n_cg)

MM = int(au_mm*cg_mm)

print(MM)
