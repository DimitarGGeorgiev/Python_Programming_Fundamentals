lines = int(input())
total_water = int(0)

for i in range (0, lines):
    liters = int(input())
    total_water += liters
    if total_water > 255:
        print("Insufficient capacity!")
        total_water -= liters
        continue

print(total_water)
        

