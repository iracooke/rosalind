def line2edge(l,s):
	p,c,lloc,llen = l.rstrip().split()
	lloc=int(lloc)-1
	llen=int(llen)
	label = s[lloc:lloc+llen]
	return( (p,c,lloc,llen,label) )

def get_numtips(node,data):
	children = data[node]['children']
	n=0
	for c in children:
		if ( len(data[c]['children'])==0 ):
			n+=1
		else:
			n+=get_numtips(c,data)
	return(n)

def get_fulllabel(node,data):
	if node['parent']==None:
		return('')
	else:
		return(get_fulllabel(data[node['parent']],data)+node['label'])


# fin = open("inputs/62LREP.txt")
fin = open("inputs/rosalind_lrep.txt")
text = fin.readline().rstrip()
k = int(fin.readline().rstrip())

edge_defs = [line2edge(line,text) for line in fin.readlines()]

nodes={}

for edge in edge_defs:
	p,c,lloc,llen,label = edge

	pnode = nodes.get(p,{'children':[],'location':0,'label':'','parent':None,'name':p})
	pnode['children'].append( c )	
	nodes[p]=pnode

	cnode = nodes.get(c,{'children':[],'location':lloc,
		'label':label,'parent':p,'name':c})
	nodes[c]=cnode

candidates=[]
for name,data in nodes.items():
	data['n_descendants']=get_numtips(name,nodes)

	if(data['n_descendants']>=k):
		fl=get_fulllabel(data,nodes)
		candidates.append( (fl,len(fl)) )


candidates = sorted(candidates,key=lambda tup:tup[1])
print(candidates[-1][0])
