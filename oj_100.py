import sys 
import functools
@functools.lru_cache(None)
def find_max_cycle(n):
	num=1
	while n!=1 :
		num +=1

		if n %2 ==1:
			n=3*n +1
		else:
			n=n/2
	return num

if __name__=='__main__':
	
	for line in sys.stdin:
		try:
			i,j=map(int,line.split()[:2])
			st,end=min(i,j),max(i,j)
			print(i,j,max(find_max_cycle(n) for n in range(st,end+1)))	
		except:
			pass