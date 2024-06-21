import random
def head():
    a=4
    for i in range(1,2*a):
        space="  "*(a-1)
        star="* "
        if i==a:
            print(star*(a+1))
        else:
            print(star+space+star)
def tail():
    a=4
    for i in range(1,2*a):
        space="  "*(a)
        star="* "
        if i==1:
            print(star*(2*a))
        else:
            print(space+star)
            
 #program execution
for i in range(1,5):       
    print("--Welcome to Google Toss 2.0--")        

    print("select your choice if head press H or tail press T-")
    choice=input().lower()


    list1=["t","h"]
        
    randomchoice=random.choice(list1)
    if randomchoice=="t":
            tail()
    elif randomchoice =='h':
            head()
    if choice==randomchoice:
        print("Congratulation! you have Won the Toss")
    else:
        print("Bad luck you have lost the Toss")
        


    
    

