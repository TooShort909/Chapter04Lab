total = 0
while True:
    number = float(input("Enter a positive number (or a negative number to stop): "))
    if number < 0:
        break
    total += number
print(f"The total sum is: {total}")