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

	def leaves(self):
		if len(self.children)==0:
			return([self.name])
		l=[]
		for c in self.children:
			l = l + c.leaves()
		return(l)

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

# Splits for all child nodes and descendents
def get_splits(node,taxa):
	all_splits=[]
	for c in node.children:
		lvs = c.leaves()
		nt=0
		nf=0
		ss=""
		for t in taxa:
			if t in lvs:
				ss+="1"
				nt+=1
			else:
				nf+=1
				ss+="0"
		if ( nt > 1 ) and ( nf > 1 ): # Exclude trivial splits
			all_splits.append(ss)
			child_splits = get_splits(c,taxa)
			all_splits = all_splits + child_splits

	return(all_splits)



#fin = open("inputs/56CTBL.txt")
fin = open("inputs/rosalind_ctbl.txt")


inputs = fin.readlines()
nwk = inputs[0].rstrip()

tree = Node(nwk,None)

taxa = sorted(tree.named_nodes.keys())

for s in get_splits(tree,taxa):
	print(s)



