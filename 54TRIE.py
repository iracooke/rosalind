

# input="inputs/54TRIE.txt"
input="inputs/rosalind_trie.txt"

with open(input) as f:
	strings=[line.rstrip() for line in f]

def get_descendants(strings,root_num):
	branches={}
	for s in strings:
		if (len(s)>0):
			c=s[0]
			if len(s)>1:
				csuff=s[1:]
			else:
				csuff=""			

			if branches.get(c) == None:
				branches[c]=[csuff]
			else:
				branches[c]=branches[c]+ [csuff]



	trie=[]

	next_node_num = root_num + 1
	for c,branch in branches.items():
		edge = (root_num , next_node_num , c)
		edge_desc = get_descendants(branch,next_node_num)
		next_node_num+=(len(edge_desc)+1)

		trie = trie + [edge]
		trie = trie + edge_desc
	return(trie)



d = get_descendants(strings,1)

for e in d:
	print(e[0],e[1],e[2])