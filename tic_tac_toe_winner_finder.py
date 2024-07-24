def row_check(matrix,s,state):
    
    
    for i in matrix:
        count=0
        for j in i:
            if j==s:
                count+=1
        if count==3 and state:
            state =False
            if s=='O':
                print("Abhinav Wins")
            else:
                print("Anjali Wins")
    return state
                
def column_check(matrix,s,state):
    
    for i in range(3):
        count=0
        for j in range(3):
            index_matrix=matrix[j][i]
            if index_matrix==s:
                count+=1
            if count==3 and state:
                state =False
                if s=='O':
                    print("Abhinav Wins")
                else:
                    print("Anjali Wins")
    return state
def diagonal_check(matrix,s,state):
    
    count=0
    for i in range(3):
        
        for j in range(3):
            if i==j:
                index_matrix=matrix[i][j]
                if index_matrix==s:
                    count+=1
                if count==3 and state:
                    state =False
                    if s=='O':
                        print("Abhinav Wins")
                    else:
                        print("Anjali Wins")
                    
    return state
def opposite_daigonal_check(matrix,s,state):
    count=0
    
    for i in range(3):
        diagonal_col_index=3-i-1
        matrix_acess=matrix[i][diagonal_col_index]
        if matrix_acess==s:
            count+=1
        if count==3:
            state =False
            if s=='O':
                        print("Abhinav Wins")
            else:
                        print("Anjali Wins")
    return state
print("Welcome to Tic Tac Toe Winner Announcer")  
print("X = input of Anjali")
print("O =input of Abhinav")
print("To win --column or row or Diagonal should be same either X or O-- ")
print("3 X 3 tic tac toe input matrix to find who is winner")
matrix=[]
state=True
for i in range(3):
    print("Enter Row {} with space".format(i+1))
    inputmatrix=input().upper().split()
    matrix+=[inputmatrix]
diagonal_o=diagonal_check(matrix,"O",state)
diagonal_x=diagonal_check(matrix,"X",diagonal_o)
opposite_daigonal_o=opposite_daigonal_check(matrix,'O',diagonal_x)
opposite_daigonal_x=opposite_daigonal_check(matrix,'X',opposite_daigonal_o)

row_check_x=row_check(matrix,'X',opposite_daigonal_x)
row_check_o=row_check(matrix,'O',row_check_x)
column_check_o=column_check(matrix,'O',row_check_o)
column_check_x=column_check(matrix,'X',column_check_o)
if column_check_x:
    print("Tie")





