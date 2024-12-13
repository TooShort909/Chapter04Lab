tuition = 8000
for year in range(1, 6):
    tuition *= 1.03  # 3% increase each year
    print(f"Year {year}: ${tuition:.2f}")