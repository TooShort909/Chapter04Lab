years = int(input("Enter number of years: "))
total_rainfall = 0
months = 0

for year in range(1, years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for year {year}, month {month}: "))
        total_rainfall += rainfall
        months += 1

average_rainfall = total_rainfall / months
print(f"Total rainfall: {total_rainfall} inches")
print(f"Average monthly rainfall: {average_rainfall} inches")