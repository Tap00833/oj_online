
import sys
def original_dic_set_up(n):

	"""{0:[],1:[],....n:[]}
	"""
	original_dic={i:[i] for i in range(n)}
	return original_dic

def find_stack(x,dic): # find which stack the given block in  type 
	block=[k for k,v in dic.items() if x in v]

	return block[0]

def move_uppen_block(stack,x,dic): # move blocks up block x to its original position

	ix=[ix for ix,bl in enumerate(dic[stack]) if bl==x][0]  # ix the slice position (position of that block)
	upper_x=dic[stack][ix:]
	dic[stack][ix:]=[]

	for bl in upper_x[1:]:
		dic[bl].append(bl)
	return upper_x  # the block upper x of that stack 

def move_onto(a,b,dic):

	"""where a and b are block numbers, puts block a onto block b after returning any blocks that 
	are stacked on top of blocks a and b to their initial positions.
	"""
	stacka=find_stack(a,dic)
	stackb=find_stack(b,dic)
	if stacka==stackb:
		pass
	else:
		up_a=move_uppen_block(stacka,a,dic)
		up_b=move_uppen_block(stackb,b,dic)
		dic[stackb].append(b)
		dic[stackb].append(a)
	

def move_over(a,b,dic):

	"""where a and b are block numbers, puts block a onto the top of the stack containing block b,
	after returning any blocks that are stacked on top of block a to their initial positions.
	"""
	stackb=find_stack(b,dic)
	stacka=find_stack(a,dic)
	if stacka==stackb:
		pass
	else:
		move_uppen_block(stacka,a,dic)
		dic[stackb].append(a)



def pill_onto(a,b,dic):  
	""" where a and b are block numbers, moves the pile of blocks consisting of block a, 
	and any blocks that are stacked above block a, onto block b.
	All blocks on top of block b are moved to their initial positions prior to the pile taking place. 
	The blocks stacked above block a retain their order when moved.
	"""
	stackb=find_stack(b,dic)
	stacka=find_stack(a,dic)
	if stacka==stackb:
		pass
	else:
		upper_b=move_uppen_block(stackb,b,dic) # all blocks on top of b moved to their initial position	
		dic[stackb].append(b)
		ix=[ix for ix,bl in enumerate(dic[stacka]) if bl==a][0]  # ix the slice position (position of that block)	
		upper_x=dic[stacka][ix:]
		dic[stacka][ix:]=[]
		dic[stackb].extend(upper_x)  # and blocks stacked above block a retain their oreder

def pill_over(a,b,dic):

	"""where a and b are block numbers, puts the pile of blocks consisting of block a, and any blocks that are stacked above block a, 
	onto the top of the stack containing block b. The blocks stacked above block a retain their original order when moved.
	"""
	stackb=find_stack(b,dic)
	stacka=find_stack(a,dic)
	if stacka==stackb:
		pass
	else:
		ix=[ix for ix,bl in enumerate(dic[stacka]) if bl==a][0]  # ix the slice position (position of that block)	
		upper_x=dic[stacka][ix:]
		dic[stacka][ix:]=[]
		dic[stackb].extend(upper_x)  # and blocks stacked above block a retain their oreder


def print_out(dic):
	for i in range(n):
		out_put=dic[i]
		if len(out_put)==0:
			print('{0}:'.format(i),end="")
			print('\n',end="")
		else:
			print('{0}: '.format(i),end="")
			for sto in out_put[:-1]:
				print('{0} '.format(sto),end ="")
			print(out_put[-1])

if __name__=='__main__':
	count=0
	for line in sys.stdin:
		count+=1
		if count==1:
			n=line.split(' ')[0]
			n=int(n)
			dic=original_dic_set_up(n)
		else:
			try:
				do1,a,do2,b=line.split(' ')
				a=int(a)
				b=int(b)
				if a==b:
					continue
				if do1=='move' and do2=='onto':
					move_onto(a,b,dic)
				elif do1=='move' and do2=='over':
					move_over(a,b,dic)
				elif do1=='pile' and do2=='onto':
					pill_onto(a,b,dic)
				elif do1=='pile' and do2=='over':
					pill_over(a,b,dic)
				else :
					print('sth wrong')
			except:
				pass
	print_out(dic)
	

		



	
