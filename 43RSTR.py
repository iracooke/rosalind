import math

# seq='ATAGCCGA'
# x=0.6
# N=90000

N=92679
x=0.466402
seq='AAGAGCTC'




na = seq.count('A')
nt = seq.count('T')
ng = seq.count('G')
nc = seq.count('C')

p_at = (1-x)/2
p_gc = x/2

pseq = math.pow(p_at,na+nt)*math.pow(p_gc,ng+nc)

p_not = math.pow(1-pseq,N)

print('{0:0.3f}'.format(1-p_not))