
import numpy as np 
lx=[]
h,w=5,5
test_array=[[1,1,0,1,1],
            [1,1,0,0,1],
            [1,1,1,0,1],
            [0,0,0,0,0],
            [0,1,1,1,1]]
state='ot'
count=0
for i in range(h):
    for j in range(w):
        if state=='ot':
            if test_array[i][j]==1:
                row_num=i
                col_num=j
                state='itt'
            else:
                pass
        else:
            pass


        if state=='itt':
            if j==w-1:
                stop_col=j
                state='ot'
                count+=1
                #print(row_num,col_num,stop_col)
                lx.append([count,row_num,col_num,stop_col,0])

            if test_array[i][j]==0:
                assert i==row_num
                stop_col=j-1
                state='ot'
                count+=1
                #print(row_num,col_num,stop_col)
                lx.append([count,row_num,col_num,stop_col,0])
         

print(np.array(lx))



    
    




def chech_overlap(l1,l2):
    if l2[2]>=l1[3]: # 下一行头 在前一行的尾巴 的后面
        return False 
    elif l2[3]<=l1[2]: # 下一行的尾 在前一行头的 前面 
        return False 
    else:
        return True 


def reset_group_num(last_row_line_num,i,lx):
    for x in range(last_row_line_num,i):
        overlap=chech(lx[last_row_line_num],lx[i])
        if overlap:
            lx[i][4]=min(lx[last_row_line_num][4],lx[i][4])
            lx[x][4]=min(lx[last_row_line_num][4],lx[i][4])


row_num=0 
current_group=1
ele_num=0 # how many in last line 
for i in range(len(lx)): # i always means the current line num

    if current_row==0: 
            lx[i][4]=current_group
            current_group+=1
            ele_num+=1
    else:

        if row_num==lx[i][1]:  # this means in this row 
            reset_group_num(last_row_line_num,i,lx)
            ele_num+=1



       
        else:
            row_num=lx[i][1]  # this means a new line begin 
            last_row_line_num=i-ele_num
            reset_group_num(last_row_line_num,i,lx)
            ele_num=1

            

       


row_num=1
current_group=1
ele_num=0 # how many in last line 
for i in range(len(lx)): # i always means the current line num

   
    if row_num==lx[i][1]:  # this means in this row 
        
        if current_row==0: 
            lx[i][4]=current_group
            current_group+=1
            ele_num+=1
        else:


            reset_group_num(last_row_line_num,i,lx)
            ele_num+=1



       
    else:
        row_num=lx[i][1]  # this means a new line begin 
        last_row_line_num=i-ele_num
        reset_group_num(last_row_line_num,i,lx)
        ele_num=1



n=len(lx)-1
row_num=h-1
e_num=0

while n>=1:
    enter_line=lx[n]
    
    if enter_line[1]==row_num:
        
        if enter_line[1]==h-1: #this is the downmost line 
            e_num+=1
        else:
            reset_group_num(this_line_st,last_row_line_num,n,lx)
            e_num=+1
    else:
        if (row_num -1) != enter_line[1]: # this means a empty line 
            pass 
        
        else: # this means a new line begin 
            
            row_num=row_num-1  # this means a new line begin  
            this_line_st=n
            last_row_line_num=n+e_num         
            reset_group_num(this_line_st,last_row_line_num,n,lx) #check overlap
            ele_num=1
        
        # this means a new line begin

    n-=1
    
print(np.array(lx))

