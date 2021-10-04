faro_string = [str(num) for num in input().split(" ")]
shuffle_times = int(input())
cycle_times = int(len(faro_string)/2)
faro_first_half = faro_string[:cycle_times:]
faro_second_half = faro_string[cycle_times::]
faro_shuffled = []
position_counter = int(0)

for i in range(0, shuffle_times):
    faro_shuffled.clear()
    position_counter = 0
    for j in range (0, cycle_times):
        faro_shuffled.insert(position_counter, faro_first_half[j])
        position_counter += 1
        faro_shuffled.insert(position_counter,faro_second_half[j])
        position_counter += 1
    faro_first_half = faro_shuffled[:cycle_times:]
    faro_second_half = faro_shuffled[cycle_times::]

print(faro_shuffled)