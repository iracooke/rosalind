

def str2set(string):
	parts=string.lstrip("{").rstrip("}").split(",")
	return(set([int(p) for p in parts]))


# fin = open("inputs/51SETO.txt")
fin = open("inputs/rosalind_seto.txt")
n,s1,s2=[line.rstrip() for line in fin.readlines()]

n=int(n)
sn = set([i for i in range(1,n+1)])
s1=str2set(s1)
s2=str2set(s2)

#1. Union
print(s1.union(s2))

#2. Intersection
print(s1.intersection(s2))

#3. A-B
print(s1-s2)

#4. B-A
print(s2-s1)

#5. Ac
print(sn-s1)

#6. Bc
print(sn-s2)