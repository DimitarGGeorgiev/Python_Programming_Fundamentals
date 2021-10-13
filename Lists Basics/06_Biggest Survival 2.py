input_string = [int(num) for num in input().split(" ")]
numbers_to_remove = int(input())
number_to_remove = int()


for i in range (0, numbers_to_remove):
    number_to_remove = min(input_string)
    input_string.remove(number_to_remove)


end_string = [str(x) for x in input_string]
print(", ".join(end_string))
