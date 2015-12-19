#!/usr/local/bin/python3

import numpy as np
import operator

def best_path(perm,sequence):

	grid = np.zeros([n+1,n+1],dtype=int)
	pathstrings = np.empty([n+1,n+1],dtype='S10000')

	for i in range(1,n+1):
		# print (i)

		for j in range(1,n+1):
			inward_scores = [grid[i-1,j],grid[i,j-1]]

			inward_paths = [pathstrings[i-1,j],pathstrings[i,j-1]]
			if perm[i-1]==sequence[j-1]:
				inward_scores.append(grid[i-1,j-1]+1)
				new_string = pathstrings[i-1,j-1].decode('UTF-8') + " " + str(perm[i-1])
				inward_paths.append(new_string)
			
			max_index, max_value = max(enumerate(inward_scores), key=operator.itemgetter(1))
			grid[i,j]=max_value
			# import pdb; pdb.set_trace()
			pathstrings[i,j] = inward_paths[max_index]

	return pathstrings[n,n].decode('UTF-8')


with open("inputs/24LGIS.txt") as f:
    content = f.readlines()

n = int(content[0])

perm = [int(i) for i in content[1].split(' ')]
increasing = [int(i) for i in range(1,n+1)]

# print(n," : ",perm)

print(best_path(perm,increasing))
print(best_path(perm,increasing[::-1]))