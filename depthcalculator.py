a=8
for i in range(8,1):
    spaces=" "*i
    star="* "
    middlespace="  "*(a-(2*i-1))
    if i==1 or i==a:
        print(space+(star*i))
    else:
        print(space+star+middlespace+star)