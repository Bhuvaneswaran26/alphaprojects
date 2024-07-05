def for_fib(n):
    print("fibonacci_series using for Loop")
    a=0
    b=1
    print(0)
    for i in range(n-1):
       print(b)
       c=a
       a=b
       b=a+c 
def while_fib(n):
    print("fibonacci_series using while Loop")
    a=0
    b=1
    print(0)
    i=0
    while(i<n-1):
       print(b)
       c=a
       a=b
       b=a+c 
       i+=1

def recursion_fib(n):

    

    if n<=1:
        return n
    else:
        return recursion_fib(n-1)+recursion_fib(n-2)

print("Enter the number")
num=int(input())
print("Fibonacci_series using recursion")      
for i in range(num):
    r=recursion_fib(i)
    print(r)
for_fib(num)
while_fib(num)
