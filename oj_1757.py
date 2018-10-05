
import sys

##set up edge relation ship 
## l: node1-node2 node1-node2 like this and form a direct graph  
##graph set up 
## a:[its neighbor]
## dfs to find the connectivity 

def  find_all(l):

	""" Thia function will return a list that contain all node 
	and this list is the row and col of the adjacency matrix 
	"""
	all_node=[]
	for i in l:
		if i not in all_node:
			all_node.append(i)
		else:
			pass
	return all_node


def graph_setup(l):

	"""This function is for setup a graoph that record node and its neighbor adjacency list
	"""
	all_node=find_all(l)
	graph_dic={node:[] for node in all_node} # graph setup 
	i=0
	while i < len(l):
		if l[i+1] not in graph_dic[l[i]]:
			graph_dic[l[i]].append(l[i+1])
			i=i+2
		else:
			i=i+2
	return graph_dic 






def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

	

def check_connected(a,b,graph_dic):
	leaves=dfs(graph_dic,a)
	if b in leaves:
		return True
	else:
		return False


def check_replaceble(word1,word2,graph_dic):
	if len(word1) != len(word2):
		return False
	else:
		rep=True
		for i in range(len(word1)):
			#print(word1[i],word2[i])
			if word1[i]==word2[i]:
				continue
			if word1[i] not in graph_dic.keys() or word2[i] not in graph_dic.keys():
				rep=False
				break
			else:
				rep=check_connected(word1[i],word2[i],graph_dic)
				if rep==False:
					break
		return rep



if __name__=='__main__':	
	count=0
	startpos=1
	for line in sys.stdin:
		if count==startpos-1:
			gr,wr=map(int,line.split(' ')[:2])
			#
			#print(gr,wr)
			l=[]
			count+=1

		else:

			if count in range(startpos,startpos+gr):
				xx=line.strip().split(' ')[:2]
				#print(xx)
				l.extend(xx)
				#print(xx)
				#print('count:{0},startpos,endpos:{1} {2}'.format(count,startpos+1,startpos+gr+1))
				count+=1

				
				if count==startpos+gr:
					graph_dic=graph_setup(l)
			
					#print('dic setup')	
					continue
			
			if count in range(startpos+gr,startpos+gr+wr):
				
				
				word1,word2=line.strip().split(' ')[:2]	
				#print('text')
				#print(word1,word2)
				#print('count:{0},startpos,endpos:{1} {2} word2 {3}'.format(count,startpos+gr+1+1,startpos+gr+wr+1+1,word2))
				if check_replaceble(word1,word2,graph_dic):
					print('yes')
				else:
					print('no')
				count+=1
				
			if count==startpos+gr+wr:
				startpos=startpos+gr+wr+1
				#print('nst')


     
        		
        		

        

# if __name__=='__main__':	
# 	linenum=0
# 	start=1
# 	print('############')
# 	for line in sys.stdin:
# 		if linenum==start-1 :
# 			gr,wr=map(int,line.split(' ')[:2])
# 			print(gr,wr)
# 			print('input number {}'.format(line))
# 			linenum+=1

# 		else:

# 			if linenum in range(start,start+gr):
# 				print('input dic {}'.format(line))
# 				linenum+=1

				
# 				if linenum==start+gr:
# 					print('graph set up')

# 				continue

			
# 			if linenum in range(start+gr,start+gr+wr):
# 				print('text:{}'.format(line))
# 				linenum+=1
				
# 			if linenum==start+gr+wr:
# 				start=start+gr+wr+1
# 				print('new start')















