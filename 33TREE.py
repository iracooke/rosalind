import sys

def read_node(fp):

	for line in fp:
		line = line.rstrip()
		if line.startswith(">"):
			if name: yield (name, ''.join(seq))
			name, seq = line[1:], []
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))


fin = open("inputs/33TREE.txt")

n = int(fin.readline())
edges = [  line.rstrip().split(' ') for line in fin]

num_needed = n - 1 - len(edges)
print(num_needed)

# A list of sets with nodes belonging to subgraphs
subgraphs=[]

for edge in edges:
	subgraph_indexes=[]

	for node in edge:
		for i in range(0,len(subgraphs)):
			subgraph=subgraphs[i]
			if node in subgraph:
				subgraph_indexes.append(i)

	if len(subgraph_indexes)==0:
		subgraphs.append( {edge[0],edge[1]}  )
	elif len(subgraph_indexes)==1:
		subgraphs[subgraph_indexes[0]].update({edge[0],edge[1]})
	else:
		ia,ib=subgraph_indexes
		subgraphs[ib].update(subgraphs.pop(ia))


print(subgraphs)


