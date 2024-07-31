def check_prime(n):    
    flag=0
    for i in range(1,n+1):
        if(n%i==0):
            flag=flag+1
    if(flag==2):
        return "is PRIME"
    else:
        return "is NOT PRIME"


def even_check(n):
    sum=0
    while(n>0):
        last_digit = n%10
        sum = sum + last_digit
        n=n//10
    if(sum%2==0):
        return "is EVEN"
    else:
        return "is NOT EVEN"

for i in range(100,201):
    print(f"{i} {check_prime(i)} & sum of digits {even_check(i)}")  
