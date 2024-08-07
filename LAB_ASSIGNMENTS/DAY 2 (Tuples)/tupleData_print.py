monthly_incomes = (
    ("January", 5000), ("February", 5500), ("March", 6000),
    ("April", 5800), ("May", 6200), ("June", 7000),
    ("July", 7500), ("August", 7300), ("September", 6800),
    ("October", 6500), ("November", 6000), ("December", 5500)
)

months, incomes = zip(*monthly_incomes)

total_income = sum(incomes)

print(f"Total income : {total_income}\n")

quarters = [
    monthly_incomes[:3],
    monthly_incomes[3:6], 
    monthly_incomes[6:9],   
    monthly_incomes[9:]     
]

for quarter in quarters:
    quarter_total = sum(income for _, income in quarter)
    for month, income in quarter:
        print(f"{month}: {income}")
    print("--------------------")
    print(f"Quarter: {quarter_total}\n")