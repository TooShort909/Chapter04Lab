print("Celsius to Fahrenheit Table")
print("Celsius | Fahrenheit")
for celsius in range(21):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:8} | {fahrenheit:10.2f}")