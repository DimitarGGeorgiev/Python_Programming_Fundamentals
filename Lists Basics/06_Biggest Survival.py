input_string = input()
input_string_as_list = input_string.split(" ")
numbers_to_remove = int(input())
sorted_string = input_string_as_list
sorted_string.sort()

for i in range (0, numbers_to_remove):
    input_string_as_list.remove(sorted_string[0])

print(input_string)