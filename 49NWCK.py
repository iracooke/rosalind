import sys

def match_bracket(str):
	if str[0]!="(":
		print("str must start with an open bracket")
		exit()
	nopen=0
	nclose=0
	for i in range(0,len(str)):
		if str[i]=="(":
			nopen+=1
		if str[i]==")":
			nclose+=1
			if nopen==nclose:
				return(i)

	return(-1)
		

class Node(object):
	name=""
	parent=None
	children=[]
	named_nodes=None

	def ancestors(self):
		anc=[self]
		last_parent = self.parent
		while last_parent!=None:
			anc.append(last_parent)
			last_parent = last_parent.parent
		return(anc)

	def __init__(self, nwkstring, parent):
		super(Node, self).__init__()
		self.parent=parent
		self.children=[]
		self.name=""
		if parent==None:
			self.named_nodes={}
		else:
			self.named_nodes=parent.named_nodes

		if nwkstring==None or len(nwkstring)==0:
			self.name=""
		else:
			if nwkstring[-1] == ';':
				self.is_root=True

				nwkstring=nwkstring.rstrip(";")

			if (nwkstring.find(",")==-1) and (nwkstring.find("(")==-1):
				self.name=str(nwkstring.lstrip().rstrip())
			elif (nwkstring[0]=="("):
				close_i = match_bracket(nwkstring)

				if close_i==-1:
					print("No matching bracket for "+nwkstring)
					exit()
				self.name=str(nwkstring[close_i+1:])
				nwkstring=nwkstring[1:close_i]

				if nwkstring.find(",")==-1:
					self.children.append(Node(nwkstring,self))
				else:
					i=0
					next_child=""
					has_comma=False
					while i < len(nwkstring):
						c=nwkstring[i]
						if c=='(':
							iopen=i
							close_i = match_bracket(nwkstring[iopen:])
							if close_i==-1:
								print("No matching bracket for "+nwkstring+" in "+nwkstring[iopen:])

							close_i=iopen+close_i+1
							self.children.append(Node(nwkstring[iopen:close_i],self))
							next_child=""

							if (close_i+1 < len(nwkstring)) and (nwkstring[close_i+1]==","):
								has_comma=True
								i=close_i
							else:
								has_comma=False
								i=close_i-1
						elif c==",":
							if has_comma and next_child=="":
								self.children.append(Node("",self))
							has_comma=True
							if next_child!="":
								self.children.append(Node(next_child,self))
							next_child=""
						else:
							next_child = next_child+c

						i+=1
					if(has_comma):

						self.children.append(Node(next_child,self))
			else:
				print("Invalid Newick")
				exit()
		if self.name!="":
			self.named_nodes[self.name]=self 



	def __str__(self):
		if ( len(self.children) == 0):
			return(self.name)
		else:
			return(self.name + " children: " + str([str(child) for child in self.children]))			


def read_example(fp):
	tree, node_pair = None, []
	for line in fp:
		line = line.rstrip()
		if line=='':
			yield (tree,node_pair)
			tree, node_pair = None, []
		else:
			if tree:
				node_pair=line.split(' ')
			else:
				tree=line

	yield(tree,node_pair)



# fin = open("inputs/49NWCK.txt")

fin = open("inputs/rosalind_nwck.txt")
distances=[]
for nwk,pair in read_example(fin):
	if(len(pair)==2):
		tree = Node(nwk,None)

		x = tree.named_nodes[pair[0]]
		y = tree.named_nodes[pair[1]]

		xa = x.ancestors()
		ya = y.ancestors()

		ydist=0
		for ya_i in ya:
			if ( ya_i in xa):
				break
			ydist+=1
		
		xdist=0
		for xa_i in xa:
			if ( xa_i in ya):
				break
			xdist+=1


		distances.append(xdist+ydist)

print(' '.join(map(str,distances)))


