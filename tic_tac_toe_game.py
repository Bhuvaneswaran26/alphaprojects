def all_function(matrix):
    diagonal_o=diagonal_check(matrix,"O",state)
    diagonal_x=diagonal_check(matrix,"X",diagonal_o)
    opposite_daigonal_o=opposite_daigonal_check(matrix,'O',diagonal_x)
    opposite_daigonal_x=opposite_daigonal_check(matrix,'X',opposite_daigonal_o)

    row_check_x=row_check(matrix,'X',opposite_daigonal_x)
    row_check_o=row_check(matrix,'O',row_check_x)
    column_check_o=column_check(matrix,'O',row_check_o)
    column_check_x=column_check(matrix,'X',column_check_o)
    return column_check_x


def input_data(matrix,name,dice):
    
    print("{} Enter the index of --Row-- and --Column-- you are {} holder".format(name,dice))
    index_data=input().split()
    
    row=int(index_data[0])
    col=int(index_data[1])
    if matrix[row][col]==1:
            matrix[row][col]=dice
            for i in matrix:
                print(i)
            state=all_function(matrix)

            return matrix,state
    else:
            print("Already Entered")
            input_data(matrix,name,dice)
def row_check(matrix,s,state):
    
    
    for i in matrix:
        count=0
        for j in i:
            if j==s:
                count+=1
        if count==3 and state:
            state =False
            if s=='O':
                print("{} Congratulation.. you have won the Game".format(player2_name))
            else:
                print("{} Congratulation... you have won  the Game".format(player1_name))
           
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
                    print("{} Congratulation.. you have won the Game".format(player2_name))
                else:
                    print("{} Congratulation... you have won the Game".format(player1_name))
                
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
                        print("{} Congratulation.. you have won the Game".format(player2_name))
                    else:
                        print("{} Congratulation... you have won the Game".format(player1_name))
                    
                    
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
                        print("{} Congratulation.. you have won the Game".format(player2_name))
            else:
                        print("{} Congratulation... you have won the Game".format(player1_name))
            
    return state

   
    

#program Execution
print("Player_1 Enter your Name")
player1_name=input()
print("Player_2 Enter your Name")
player2_name=input()
print("Note {} you are --X-- dice Holder {} --O-- dice holder".format(player1_name,player2_name))
matrix=[[1,1,1],[1,1,1],[1,1,1]]
state=True
i=0
while(True):

   if state :
        matrix,state=input_data(matrix,player1_name,"X")
        i+=1
        
        if state and i==9:
            print("Tie")
            break
        elif state:
             
            matrix,state=input_data(matrix,player2_name,"O")
            i+=1
        
   elif state and  i==9:
        print("Tie")
        break
   elif not state:
        break
   
        