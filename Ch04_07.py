days = int(input("Enter the number of days: "))
total_pay = 0
pennies = 1  # start with 1 penny on the first day

print("Day | Salary")
for day in range(1, days + 1):
    total_pay += pennies
    print(f"{day:3} | ${pennies / 100:.2f}")
    pennies *= 2  # salary doubles each day

print(f"Total pay after {days} days: ${total_pay / 100:.2f}")