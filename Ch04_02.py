budget = float(input("Enter your monthly budget: "))
total_expenses = 0
while True:
    expense = float(input("Enter an expense (or a negative number to stop): "))
    if expense < 0:
        break
    total_expenses += expense
print(f"Total expenses: {total_expenses}")
print(f"Budget remaining: {budget - total_expenses}")