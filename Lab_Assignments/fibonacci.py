n=int(input("Enter a number\n"))

def fibo(n):
    if(n==0 or n==1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(n):
    print(fibo(i),end=" ")