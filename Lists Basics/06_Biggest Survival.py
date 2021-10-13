input_string = [int(num) for num in input().split(" ")]
numbers_to_remove = int(input())
sorted_string = input_string.copy()
sorted_string.sort()

for i in range (0, numbers_to_remove):
    input_string.remove(sorted_string[i])

print(input_string)