def rotate90(string):
    temp=[]
    for i in string:
        temp+=[i.copy()]
    for i in range(n):
       for j in range(n-1,-1,-1):
            temp[i][n-1-j]=string[j][i]
    return temp
def convert(m):
    return int(m)
n=int(input())
matrix=[]
for i in range(n):
    a=input().split()
    res=list(map(convert,a))
    matrix+=[res]
original_matrix=matrix.copy()
choice=True
sum_of_rotation=0
while(True):
    indata=input().split()
    operation=indata[0]
    if operation=="R":
        angle=int(indata[1])
        sum_of_rotation+=angle
        angle=angle//90
        for i in range(angle):
            matrix=rotate90(matrix)
    elif operation=="Q":
        index_1=int(indata[1])
        index_2=int(indata[2])
        print(matrix[index_1][index_2])
    elif operation=="-1":
        break
    elif operation=="U":
        index_1=int(indata[1])
        index_2=int(indata[2])
        data=int(indata[3])
        original_matrix[index_1][index_2]=data
        matrix=original_matrix
        for i in range(sum_of_rotation//90):
            matrix=rotate90(matrix)
        
           
        
        
    
    
    