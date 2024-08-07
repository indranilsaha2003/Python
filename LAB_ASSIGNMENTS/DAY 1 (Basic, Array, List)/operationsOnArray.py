arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_all_num(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def sum_all_odd_num(list):
    sum = 0
    for i in list:
        if(i % 2 != 0):
            sum += i
    return sum

def sum_all_even_num(list):
    sum = 0
    for i in list:
        if(i % 2 == 0):
            sum += i
    return sum

def count_of_odd_num(list):
    count = 0
    for i in list:
        if(i % 2 != 0):
            count += 1
    return count

def count_of_even_num(list):
    count = 0
    for i in list:
        if(i % 2 == 0):
            count += 1
    return count

def list_of_even_num(list):
    even = []
    for i in list:
        if(i % 2 == 0):
            even.append(i)
    return even

def list_of_odd_num(list):
    idx = 0
    odd = []
    for i in list:
        if(i % 2 != 0):
            odd.append(i)
        idx += 1
    return odd

def print_num(list):
    for i in list:
        print(i, end=" ")
    print()

def operation(arr):
    list = []
    list.append(sum_all_num(arr))
    list.append(sum_all_odd_num(arr))
    list.append(sum_all_even_num(arr))
    list.append(count_of_odd_num(arr))
    list.append(count_of_even_num(arr))
    list.append(list_of_even_num(arr))
    list.append(list_of_odd_num(arr))
    return list

finallist = operation(arr)
print_num(finallist)
