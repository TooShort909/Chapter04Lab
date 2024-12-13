speed = float(input("Enter the speed of the vehicle in mph: "))
time = int(input("Enter the number of hours traveled: "))

for hour in range(1, time + 1):
    distance = speed * hour
    print(f"Hour {hour}: {distance} miles")