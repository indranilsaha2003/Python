def ap1(list):
    n = len(list)
    temp = list[0]
    list[0] = list[n-1]
    list[n-1] = temp
    return list

def ap2(list):
    n = len(list)
    list[0] = list[0] + list[n-1]
    list[n-1] = list[0] - list[n-1]
    list[0] = list[0] - list[n-1]
    return list

def ap3(list):
    n = len(list)
    list[0] = list[0] ^ list[n-1]
    list[n-1] = list[0] ^ list[n-1]
    list[0] = list[0] ^ list[n-1]
    return list

def ap4(list):
    n = len(list)
    list[0], list[n-1] = list[n-1], list[0]
    return list

def print_num(list):
    for i in list:
        print(i, end=" ")
    print()

arr = [1, 2, 3, 4, 5, 6]
ans = []
n = int(input("Enter which approach you want to verify (1-4)\n"))
if n == 1:
    ans = ap1(arr)
elif n == 2:
    ans = ap2(arr)
elif n == 3:
    ans = ap3(arr)
else:
    ans = ap4(arr)
print_num(ans)