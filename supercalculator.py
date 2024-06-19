def calculator(c,d,opr):
    if opr=='+':
        print(a+"="+str(c+d))
    elif opr=='-':
        print(a+"="+str(c-d))
    elif opr=='*':
        print(a+"="+str(c*d))
    elif opr=='/':
        print(a+"="+str(c/d))
    elif opr=="//":
        print(a+"="+str(c//d))
    elif opr=="**":
        print(a+"="+str(c**d))
    
    
#Program execution
print("---supercalculator---")
print('perform calculation')       
for i in range(20):  
    count=0  
    a=input()
    first_number=""
    second_number=""
    opr=""#operation
    s=True
    for i in a:
        if i.isdigit() and s:#Read firstnumber
            first_number+=i
        elif s or (count<2 and not(i.isdigit())):#store only symbols
            s=False
            opr+=i
            count+=1
        elif i.isdigit():#read secondnumber
            second_number+=i
    first_number=int(first_number)
    second_number=int(second_number)
    calculator(first_number,second_number,opr)
    
            