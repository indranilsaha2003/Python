def averages_from_tuples(nums):
    # Unzip the tuples into separate lists
    col1, col2, col3 = zip(*nums)
    
    # Calculate the averages using list comprehension
    averages = [sum(col) / len(nums) for col in (col1, col2, col3)]
    
    return averages


nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
result = averages_from_tuples(nums)
print(f"Resultant list of averages : {result}")
