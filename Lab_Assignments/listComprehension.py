lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]


# Convert each tuple to a list using list comprehension
lst_lists = [list(tup) for tup in lst_tuples]


print(lst_lists)
