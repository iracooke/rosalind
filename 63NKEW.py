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
	weight=0

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

		# print("Init with: "+nwkstring)

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
				self.name,self.weight=nwkstring.lstrip().rstrip().split(":")
				self.weight=float(self.weight)

			elif (nwkstring[0]=="("):
				close_i = match_bracket(nwkstring)

				if close_i==-1:
					print("No matching bracket for "+nwkstring)
					exit()
				# import pdb;pdb.set_trace()
				self.name=str(nwkstring[close_i+1:])
				# print(nwkstring)
				nwkstring=nwkstring[1:close_i]

				if self.name.count(":")==1:
					# print(self.name,nwkstring)
					self.name,self.weight = self.name.split(":")
					# print(self.weight)
					self.weight=float(self.weight)

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

							next_comma = nwkstring[iopen+close_i+1:].find(",")
							next_cb = nwkstring[iopen+close_i+1:].find(")")
							next_ob = nwkstring[iopen+close_i+1:].find("(")


							next_delims = list(filter((-1).__ne__, [next_comma,next_cb,next_ob]))





							if len(next_delims)>0:
								# import pdb;pdb.set_trace()	
								# print(next_delims)							
								next_delim = min(next_delims)
								name_candidate = nwkstring[close_i+1:next_delim+close_i+1]
								# print("Name :"+name_candidate+" "+nwkstring[close_i+1:])
								close_i=iopen+close_i+next_delim+1
								descendant = nwkstring[iopen:close_i]
							else:
								# import pdb;pdb.set_trace()																
								close_i=iopen+close_i+1
								descendant = nwkstring[iopen:]
							# if nwkstring.find("Haliaeetus_tacz"):
								

							if close_i==-1:
								print("No matching bracket for "+nwkstring+" in "+nwkstring[iopen:])

							# print("Descending "+descendant+" from "+nwkstring)
							self.children.append(Node(descendant,self))
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
								# print("Next child "+next_child+ "from: "+nwkstring)
								self.children.append(Node(next_child,self))
							next_child=""
						else:
							next_child = next_child+c

						i+=1
					if(has_comma):
						# print("Next child no comma "+next_child+ "from: "+nwkstring)
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




# fin = open("inputs/63NKEW.txt")
fin = open("inputs/rosalind_nkew.txt")
# fin = open("inputs/test.txt")

distances=[]
for nwk,pair in read_example(fin):
	if(len(pair)==2):
		tree = Node(nwk,None)

		# print(nwk,tree)

		x = tree.named_nodes[pair[0]]
		y = tree.named_nodes[pair[1]]

		xa = x.ancestors()
		ya = y.ancestors()

		# import pdb;pdb.set_trace()
		# print([a.name + ' ' +str(a.weight) for a in xa])
		# print([a.name + ' ' +str(a.weight) for a in ya])

		ydist=0
		for ya_i in ya:
			if ( ya_i in xa):
				break
			ydist+=float(ya_i.weight)
		
		xdist=0
		for xa_i in xa:
			if ( xa_i in ya):
				break
			xdist+=float(xa_i.weight)


		distances.append(int(xdist+ydist))

print(' '.join(map(str,distances)))


